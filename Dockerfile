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
# separate layer to use docker cache
RUN cd /home && \
    # clone and init the git submodules

    git clone -b master --recurse-submodules https://github.com/FFIG/ffig.git

# start a new layer to help Docker cache this step
# make directories in ffig traversable
RUN touch home/ffig/__init__.py home/ffig/ffig/templates/__init__.py

ENV PYTHONPATH $PYTHONPATH:/home/ffig/ffig/

# Copy in the content of this repository
COPY . /home/flask/
WORKDIR /home/flask/

CMD ["python", "ffig_explorer.py"]
