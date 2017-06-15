# Docker Tutorial

## Docker

* what: tool that allow users to package an application and its dependencies into **standardized** unit for development. 

* why: develop in one enviornment, deploy in another

## Terminology

1. Images
	
	* what: blueprint of application. Get an image using `docker pull`
		it is conceptually similar to a git repo.

	* base image: image with no parent image. Usually an OS image like ubuntu.

	* child image: images derived from base image

	* official image: maintained by people at Docker. Usually one word long

	* user image: build by devs at large. should be formated as:

		`user/image-name`

2. Containers

	* what: build from images. Docker's equivalent solution to **virtual machines**. Created using `docker run`

	* why: more lightweight than virtual machines, so can use underlying system/resources better

3. Data Volumes

	* what: a specially-designated directory within container(s), bypass the union file system. 

	* why: usually mount local directory onto docker container. Can develop locally
	as if in container. Then deploy the container with local codebase (somehow)

	* example:

	```	
		docker run -v /Users/lingxiao/Documents/camera-project:/root/camera-project -p 9000:9000 -p 8000:8000 -t -i bamos/openface /bin/bash
	```

4. Data Volume Containers	

5. Docker Daemon
	
	* what: background service running on host that manages 
	building, running and distributing docker containers

## Basic Hello World

1. install docker

2. check docker is properly installed:

	`docker run hello-world`

3. pull an **image** from the docker registry

	`docker pull busy-box`

4. check the image is on local disk

	`docker images`

5. run the busy box:	

	`docker run busybox echo "hello world"`

6. check all containers that are running with: `docker ps`

   check all containers that ever ran: `docker ps -a`

7. Running more than one command in a container:

	`docker run -it busybox sh`

	* allow us to run an interactive shell. Note we are now 
	in the busybox container as if it's a virtual machine
	and presumably we can develop everything in there

	* note here if we `rm -rf bin`, all shell commands are now disabled.
	  but if we exit an restart `busybox`, we see the `bin` directory is back

8. Finally, remove containers that are no longer used with
	
	`docker rm [CONTAINER-ID]`

	or rm all exited containers with:

	`
		docker rm $(docker ps -a -q -f status=exited)
	`

## Basic Docker Website

1. `docker pull prakhar1989/static-site`

2. `docker run prakhar1989/static-site` 
	
	will results in `Nginx is running ...`, but no ports are exposed. 

	* Instead run:

	`docker run -d -P --name static-site prakhar1989/static-site`

	where `-d` is detach mode, so command line is free 
	`-P` puslish all exposed ports to a random port.

	* `docker port static-site` will tell you the port at:

		`80/tcp -> 0.0.0.0:ID`

	* go to `localhost:[ID]` on browser
ne
 	* `docker stop` to detach container


## Building a Docker Image of a flask-app

1. navigate to `path/to/flask-app`

2. create a docker file named 'Dockerfile' with:

	```
		# python with some batteries
		FROM python:2.7.13-onbuild
		# flask app port number 
		EXPOSE 5000
		# running the application 
		CMD ['python', './app.py']
	```

	* Note `onbuild` will parse all requirements in the
	`requirements.txt` file and install them to the container 
	 as well

	* see: https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/
	for more information

3. build the image with:

	`docker build -t lingxiaoseas/catnip .`

4. run the image with:
	
	`docker run -p 8888:5000 lingxiaoseas/catnip`

	publish `-p` the image with 5000 on server side and 
	externally on 8888. so the syntax is:

	`HOST:CONTAINER`


## Deploying Docker on AWS

0. login if needed:

	```
		docker login
		Username: lingxiaoseas
	```

1. push project to docker repo

	`docker push lingxiaoseas/catnip`

2. see website for instructions. But there should be a 

	`Dockerrun.aws.json`

   file in toplevel directory, and it might look like this:

   	```
		{
		  "AWSEBDockerrunVersion": "1",
		  "Image": {
		    "Name": "lingxiaoseas/catnip",
		    "Update": "true"
		  },
		  "Ports": [
		    {
		      "ContainerPort": "5000"
		    }
		  ],
		  "Logging": "/var/log/nginx"
		}   	
   	```
   	where "Name" is `username/app-name`.

## Multicontainer Environments

1. `cd` into `foodtrucks-web` directory, and there should be a 		Dockerfile with:
	```
		# start from base
		FROM ubuntu:14.04
		MAINTAINER Xiao Ling <lingxiao@seas.upenn.edu>

		# install system-wide deps for python and node
		RUN apt-get -yqq update
		RUN apt-get -yqq install python-pip python-dev
		RUN apt-get -yqq install nodejs npm
		RUN ln -s /usr/bin/nodejs /usr/bin/node

		# copy our application code
		ADD flask-app /opt/flask-app
		WORKDIR /opt/flask-app

		# fetch app specific deps
		RUN npm install
		RUN npm run build
		RUN pip install -r requirements.txt

		# expose port
		EXPOSE 5000

		# start app
		CMD [ "python", "./app.py" ]
	```

	Now do:

	```
		docker build -t lingxiaoseas/foodtrucks-web .
	```
	(don't for get the dot!)

	This will take a moment as docker download ubuntu image

	2. Now we need to run elastic search. First let's see if elasticsearch is on docker:
		`python search elasticsearch`
		should return it is

	3. Now let's run elastic search:
		`
			docker run -dp 9200:9200 elasticsearch
		`
		once again, `-dp` means detached mode, and publish
		at specified ports. Now do:

		`
			curl 0.0.0.0:9200
		`	
		and we should see info you elasticsearch.

	4. Now if we try:
		`
			docker run -P lingxiaoseas/foodtrucks-web
		`
		it should say "unable to connnect" because ElasticSearch is not connected. But it is running, to confirm, run

			`docker ps`

		and we should see the container is up.

	5. Next we need to learn about Docker network.

		Note when we do `docker ps`, we see under `PORTS`:

		`0.0.0.0:9200 -> 9200/tcp, 9300/tcp`

		the `0.0.0.0` means that we are accessing from the host machine, we need to access from `foodtrucks-web`.


	6. We need to create a new network:
		```
			# create the network
			docker network create foodtrucks

			# start the ES container
			docker run -d --net foodtrucks -p 9200:9200 -p 9300:9300 --name es elasticsearch

			# start the flask app container
			docker run -d --net foodtrucks -p 5000:5000 --name foodtrucks-web lingxiaoseas/foodtrucks-web

		```

		the gist is that we need to create a private network, 
		start a container with ports for our app and elasticsearch, then run the container


## Docker Compose for multiple containers

	* automates the afore-mentioned steps

	* build the flask container

		docker build -t lingxiaoseas/foodtrucks-web .

	1. free all ports:

		`
			docker stop $(docker ps -q)
		`	


## source: 
* main source: https://prakhar.me/docker-curriculum/
* short explanation: https://www.ctl.io/developers/blog/post/what-is-docker-and-when-to-use-it/
* expose versus publish: https://www.ctl.io/developers/blog/post/docker-networking-rules/








































