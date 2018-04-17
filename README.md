At the moment, we are looking for a simple REST API with 1 endpoint. The endpoint takes POST requests with header files and type of binding you want to generate.

Implemented as a flask-app inside a Docker container with port binding to host. 

To build and run the docker image, run

```
docker pull ffig/ffig-base
docker build -t ffig/web-base:latest .
docker run -p 5000:5000 -it ffig/web-base:latest /bin/bash
```

requests_at_explorer.py is a python requests script with a sample request that you can send against port 5000 locally. 
