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

3. Docker Daemon
	
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

	`docker rm $(docker ps -a -q -f status=exited)`


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

1. see website for instructions. But there should be a 

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

Multicontainer Environments
===

1. 



## source: 
* https://prakhar.me/docker-curriculum/
* https://www.ctl.io/developers/blog/post/what-is-docker-and-when-to-use-it/








































