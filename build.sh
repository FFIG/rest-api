pip3 install --upgrade pip && pip3 install flask

ls -al ../

git clone -b master --recurse-submodules https://github.com/FFIG/ffig.git ../ffig

touch ../ffig/__init__.py ../ffig/templates/__init__.py

ls -al ../

cd -

export PYTHONPATH="${PYTHONPATH}:/home/ffig/"
