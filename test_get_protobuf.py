import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "cpp"
import test_message_pb2
import compiled_pb

msg = compiled_pb.get_a_protobuf()
print(msg)
