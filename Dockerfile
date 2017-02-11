# Defines an image that is used as the base for the FFIG web application (REST
# API). It includes the ffig-base image, the ffig source code, and the
# dependencies required for a flask web application

# Start with ffig-base image
FROM ffig/ffig-base
MAINTAINER support@ffig.org

# Install flask
RUN pip install --upgrade pip && \
    pip2 install flask && \
    pip3 install --upgrade pip && \
    pip3 install flask

# Install the ffig codebase. Use `cd` here to avoid several WORKDIR layers.
ADD https://github.com/FFIG/ffig/archive/master.zip /home/
RUN unzip home/master.zip -d home/ && \
    rm -f home/master.zip

# Copy in the content of this repository
COPY . /home/flask/

WORKDIR /home/flask/

