import os
import sys
import time

test_mode = sys.argv[1]
if test_mode == "python":
    os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
elif test_mode == "cpp":
    os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "cpp"
elif test_mode == "cpp-compiled":
    import compiled_pb
    os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "cpp"
else:
    raise ValueError("Invalid test mode")

import test_message_pb2

msg = test_message_pb2.TestMessage()

def generate_msg():
    msg.a = 1234
    msg.b = "chap" * 999
    for i in range(100):
        m = test_message_pb2.TestRepeatedA()
        for j in range(100):
            n = test_message_pb2.TestRepeatedB()
            n.e = 234456
            n.f = 1234
            m.d.append(n)
        msg.c.append(m)

    return msg

serialized = generate_msg().SerializeToString()
print(f"Serialized message length: {len(serialized)}")


def benchmark(fn):
    iters = 0
    elapsed = 0
    benchmark_time = 1
    start_time = time.time()
    while elapsed < benchmark_time:
        fn()
        iters += 1
        elapsed = time.time() - start_time
    return iters / benchmark_time

def serialize():
    msg.SerializeToString()

def deserialize():
    msg = test_message_pb2.TestMessage()
    msg.ParseFromString(serialized)

print(f"Serialize: {benchmark(serialize):.2f} / s")
print(f"Deserialize: {benchmark(deserialize):.2f} / s")
