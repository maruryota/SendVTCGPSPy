import zmq
import sys
import json

port="54321"
host="127.0.0.1"
if len(sys.argv)>1:
  host=sys.argv[1]

cxt=zmq.Context()
sock=cxt.socket(zmq.SUB)

address = f"tcp://{host}:{port}"

sock.connect(address)
sock.setsockopt(zmq.SUBSCRIBE,''.encode("utf-8"))

count = 0
data = json.loads(sock.recv())
print(data["Report"]["Time"])
print(json.dumps(data, indent=2))
count=count+1
