pip3 install --upgrade pip && pip3 install flask

cd ../ && git clone -b master --recurse-submodules https://github.com/FFIG/ffig.git

cd /ffig && git pull origin master && cd ../rest-api

touch home/ffig/__init__.py home/ffig/ffig/templates/__init__.py

export PYTHONPATH="${PYTHONPATH}:/home/ffig/"
