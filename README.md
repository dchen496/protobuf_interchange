Setup
=====

    . setup.sh

Compile protobuf C++
====================

    sudo apt-get install autoconf automake libtool curl make g++ unzip
    cd $REPO/protobuf
    git submodule update --init --recursive
    ./autogen.sh
    ./configure
    make -j24
    export LD_LIBRARY_PATH=$REPO/protobuf/src/.libs

Create virtualenv
=================

    cd $REPO
    python3 -m venv env
    . env/bin/activate

Compile protobuf Python
=======================

    cd $REPO/protobuf/python
    python setup.py install --cpp_implementation

Generate C++ & python protobuf files
===========================

    cd $REPO
    mkdir -p gen_cpp
    protoc test_message.proto --cpp_out gen_cpp
    protoc test_message.proto --python_out gen_py

Build Python extension library
==============================

    cd $REPO
    python setup.py install

Benchmark
=========

	python benchmark.py python
	python benchmark.py cpp
	python benchmark.py cpp-compiled


Get a protobuf
==============

	python test_get_protobuf.py
