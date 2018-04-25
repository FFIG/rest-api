pip3 install --upgrade pip && pip3 install flask

git clone -b master --recurse-submodules https://github.com/FFIG/ffig.git ../ffig

touch ../ffig/__init__.py ../ffig/ffig/__init__.py ../ffig/ffig/templates/__init__.py

export PYTHONPATH="${PYTHONPATH}:../ffig/:../ffig/ffig/"

