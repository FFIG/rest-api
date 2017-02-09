# Defines an image that is used as the base for the FFIG web application (REST
# API). It includes the ffig-base image, the ffig source code, and the
# dependencies required for a flask web application

# Start with ffig-base image
FROM ffig/ffig-base
MAINTAINER support@ffig.org

# Install flask
RUN pip install --upgrade pip && pip install flask
RUN pip3 install --upgrade pip && pip install flask

# Install the ffig codebase
WORKDIR /home/ffig
ADD https://github.com/FFIG/ffig-base/archive/master.zip /home/ffig/ffig

# Copy in the content of this repository
COPY . /home/ffig/rest-api

