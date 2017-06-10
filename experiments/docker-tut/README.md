# Docker Tutorial

## Docker

* what: tool that allow users to package an application and its dependencies into **standardized** unit for development. 

* why: develope in one enviornment, deploy in another

## Containers

* what: docker's equivalent solution to **virtual machines**

* why: more lightweight than virtual machines, so can use underlying system/resources better

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

	allow us to run an interactive shell. Note we are now 
	in the busybox container as if it's a virtual machine
	and presumably we can develop everything in there

8. 


## source: 
* https://prakhar.me/docker-curriculum/




































