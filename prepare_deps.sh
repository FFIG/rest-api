pip3 install --upgrade pip && pip3 install flask

git clone -b master --recurse-submodules https://github.com/FFIG/ffig.git ../ffig

touch ../ffig/__init__.py ../ffig/ffig/templates/__init__.py

export PYTHONPATH="${PYTHONPATH}:../ffig/"

apt-get install libclang-5.0-dev
export LD_LIBRARY_PATH=/usr/lib/llvm-5.0/lib:$LD_LIBRARY_PATH
