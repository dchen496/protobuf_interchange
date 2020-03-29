export REPO=$(pwd)
export LD_LIBRARY_PATH=$REPO/protobuf/src/.libs/:$REPO/env/lib/python3.6/site-packages/protobuf-3.11.4-py3.6-linux-x86_64.egg/google/protobuf/pyext/
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
export PYTHONPATH=gen_py
. env/bin/activate
