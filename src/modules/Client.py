from config import net_config
import socket
import json
import os

HOST = net_config.host  # The server's hostname or IP address
PORT = net_config.server_port        # The port used by the server

class  Client():
    def __init__(self):
        pass

    def request_simulator(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            msg = {"pass": os.environ["PS"], "req": net_config.start_sim_request} # a real dict.

            data = json.dumps(msg)

            try:
                # Connect to server and send data
                sock.connect((HOST, PORT))
                sock.sendall(bytes(data,encoding="utf-8"))
                print(f"{data = }")
                received = sock.recv(1024)
                received = received.decode("utf-8")
                print(f"{received = }")

            except:
                pass

        print('Received', received)
        return received

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     # s.sendall(int.to_bytes(9099, byteorder='little', length=1024))
#     m = {"port": 2020, "name": "abc"} # a real dict.


#     data = json.dumps(m)
#     # Create a socket (SOCK_STREAM means a TCP socket)
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     try:
#         # Connect to server and send data
#         sock.connect((HOST, PORT))
#         sock.sendall(bytes(data,encoding="utf-8"))


#         # Receive data from the server and shut down
#         received = sock.recv(1024)
#         received = received.decode("utf-8")

#     finally:
#         data = s.recv(1024)

# print('Received', repr(data))