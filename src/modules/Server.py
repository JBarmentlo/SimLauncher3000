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
            s.settimeout(10)
            s.bind((net_config.host, net_config.server_port))
            s.listen()
            while True:
                try:
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
                            reply = self.handle_request(data)
                        except:
                            pass
                        conn.sendall(bytes(json.dumps(reply), encoding="utf-8"))
                except socket.timeout:
                    pass
                self.simhandler.kill_idle_sims()
                self.simhandler.clean_dead_sims()


    def handle_request(self, data):
        if (data["pass"] != os.environ["PS"]):
            return {}
            
        if (data["req"] == net_config.start_sim_request):
            sim_port = self.simhandler.start_new_sim()
            return {"sim_port" : sim_port}

        if (data["req"] == net_config.ping_request):
            self.simhandler.ping_sim(data["port"])
            return {"pinged_sim" : data["port"]}

        if (data["req"] == net_config.kill_request):
            self.simhandler.kill_sim(data["port"])
            return {"killed_sim" : data["port"]}


