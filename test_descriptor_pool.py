print("IMPORT DESCRIPTOR POOL")
import google.protobuf.descriptor_pool
dp = google.protobuf.descriptor_pool.Default()
try:
    print(dp.FindMessageTypeByName("TestMessage"))
except:
    print("not found")

print("import compiled_pb")
import compiled_pb

try:
    print(dp.FindMessageTypeByName("TestMessage"))
except:
    print("not found")

print("wait for gdb")
import os
import signal
os.kill(os.getpid(), signal.SIGUSR1)
