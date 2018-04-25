pip2 install --upgrade pip && \
    pip2 install flask && \
    pip3 install --upgrade pip && \
    pip3 install flask

mdkir -p home

cd /home && \
    git clone -b master --recurse-submodules https://github.com/FFIG/ffig.git

cd /home/ffig && git pull origin master && cd ../

touch home/ffig/__init__.py home/ffig/ffig/templates/__init__.py

export PYTHONPATH="${PYTHONPATH}:/home/ffig/"
