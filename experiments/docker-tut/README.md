# Docker Tutorial

## Docker

* what: tool that allow users to package an application and its dependencies into **standardized** unit for development. 

* why: devleope in one enviornment, deploy in another

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



## source: 
* https://prakhar.me/docker-curriculum/


