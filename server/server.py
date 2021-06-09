from threading import Thread
import socket
import subprocess
import os
import time
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8081        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                porto = int.from_bytes(data, byteorder='little')
                print(porto)
                port_args = ["--port", str(porto), "--host", "localhost", "-logFile", "unitylog.txt"]
                proc1 = subprocess.Popen([os.environ["SIM_PATH"]] + port_args)
                conn.sendall(b"Sim open")
                time.sleep(5)
                proc1.kill()
