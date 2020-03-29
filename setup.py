from distutils.core import setup, Extension

compiled_pb = Extension(
	'compiled_pb',
	sources=['compiled_pb.cc', 'gen_cpp/test_message.pb.cc'],
	libraries=['protobuf', ':_message.cpython-36m-x86_64-linux-gnu.so'],
	include_dirs = ['./gen_cpp', './protobuf/src/', './protobuf/python/'],
	library_dirs = ['./protobuf/src/.libs/', './env/lib/python3.6/site-packages/protobuf-3.11.4-py3.6-linux-x86_64.egg/google/protobuf/pyext/'])

setup(ext_modules=[compiled_pb])
