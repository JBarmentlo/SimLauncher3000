import socket
import time
import json
import os
from modules import SimHandler
from config import net_config
import logging

logging.root.setLevel(logging.DEBUG)
ServerLogger = logging.getLogger("Server")
ServerLogger.setLevel(logging.DEBUG)

class Server():
    def __init__(self):
        self.simhandler = SimHandler()
        ServerLogger.debug(f"\n\nStarted Server Instance")


    def server_loop(self):
        '''
            Main server loop. Listens to port, launches sims, answers port numbers of sims.
        '''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)
            s.bind((net_config.host, net_config.server_port))
            s.listen()
            ServerLogger.debug(f"Socket {s} bound, listening")
            while True:
                try:
                    time.sleep(1)
                    conn, addr = s.accept()
                    with conn:
                        ServerLogger.debug('Connected by', addr)
                        data = conn.recv(1024)
                        data = data.decode("utf-8")
                        sim_port = None
                        reply = {}
                        try:
                            data = json.loads(data)
                            ServerLogger.debug(f"Msg received: {data}")
                            reply = self.handle_request(data)
                            ServerLogger.debug(f"Reply: {reply}")
                        except Exception as e:
                            ServerLogger.error(f"{e}")
                            pass
                        conn.sendall(bytes(json.dumps(reply), encoding="utf-8"))
                except socket.timeout:
                    pass
                self.simhandler.kill_idle_sims()
                self.simhandler.clean_dead_sims()


    def handle_request(self, data):
        if (data["pass"] != os.environ["PS"]):
            ServerLogger.error(f"Pass doesn match. Recieved: {data['pass']}")
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


