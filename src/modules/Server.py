import socket
import time
import json
import os
from modules import SimHandler
from config import net_config


class Server():
    def __init__(self):
        self.simhandler = SimHandler()


    def server_loop(self):
        '''
            Main server loop. Listens to port, launches sims, answers port numbers of sims.
        '''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((net_config.host, net_config.server_port))
            s.listen()
            while True:
                time.sleep(1)
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    data = conn.recv(1024)
                    data = data.decode("utf-8")
                    sim_port = None
                    reply = {}
                    try:
                        data = json.loads(data)
                        if (data["pass"] != os.environ["PS"]):
                            break
                        if (data["req"] == net_config.start_sim_request):
                            sim_port = self.simhandler.start_new_sim()
                            reply = {"sim_port" : sim_port}
                        if (data["req"] == net_config.ping_request):
                            self.simhandler.ping_sim(data["port"])
                            reply = {"pinged_sim" : data["port"]}
                    except:
                        pass
                    conn.sendall(bytes(json.dumps(reply), encoding="utf-8"))

# Port to listen on (non-privileged ports are > 1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     while True:
#         conn, addr = s.accept()
#         with conn:
#             print('Connected by', addr)
#             while True:
#                 data = conn.recv(1024)
#                 if not data:
#                     break
#                 porto = int.from_bytes(data, byteorder='little')
#                 print(porto)
#                 port_args = ["--port", str(porto), "--host", "localhost", "-logFile", "unitylog.txt"]
#                 proc1 = subprocess.Popen([os.environ["SIM_PATH"]] + port_args)
#                 conn.sendall(b"Sim open")
#                 time.sleep(5)
#                 proc1.kill()


# port_args = ["--port", str(9099), "--host", "localhost", "-logFile", "unitylog.txt"]
# proc1 = subprocess.Popen([os.environ["SIM_PATH"]] + port_args)
# proc1.kill()

