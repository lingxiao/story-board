# Docker Tutorial

## Docker

* what: tool that allow users to package an application and its dependencies into **standardized** unit for development. 

* why: develope in one enviornment, deploy in another

## Terminology

1. Images
	
	* what: blueprint of application. Get an image using `docker pull`


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

1. 


## source: 
* https://prakhar.me/docker-curriculum/




































