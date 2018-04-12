build:
	docker build -t ffig/web-base:latest .

run: build
	docker run -p 5000:5000 -it ffig/web-base:latest


clean:
	docker kill $$(docker ps -q -f ancestor=ffig/web-base)

# builds the container, 
# starts it in detached mode 
# mounts the local workdir to the flask dir
# any changes locally will go to the container
devel: build
	docker run -d -p 5000:5000 ffig/web-base:latest

# HACKY - only works with 1 running container
# starts a shell inside the running container
debug:
	docker exec -it $$(docker ps -q) /bin/bash
