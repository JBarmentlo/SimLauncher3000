import logging
from modules import PortHandler
from modules import Server

logging.basicConfig(filename="mylog.log")
logging.root.setLevel(logging.DEBUG)
s = Server()
s.server_loop()