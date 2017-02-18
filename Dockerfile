# Defines an image that is used as the base for the FFIG web application (REST
# API). It includes the ffig-base image, the ffig source code, and the
# dependencies required for a flask web application

# Start with ffig-base image
FROM ffig/ffig-base
MAINTAINER support@ffig.org

# Install flask
RUN pip2 install --upgrade pip && \
    pip2 install flask && \
    pip3 install --upgrade pip && \
    pip3 install flask

# Install the ffig codebase. Use `cd` here to avoid several WORKDIR layers.
RUN cd /home && \
    git clone -b master --recurse-submodules https://github.com/FFIG/ffig.git && \
    touch __init__.py ffig/__init__.py

# Copy in the content of this repository
COPY . /home/flask/
WORKDIR /home/flask/

CMD ["python", "ffig_explorer.py"]
