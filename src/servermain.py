import logging
from modules import PortHandler
from modules import Server

logging.basicConfig(filename="mylog.log")

s = Server()
s.server_loop()