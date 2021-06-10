from utils import DotDict

net_config = DotDict()
net_config.host = 'localhost'
net_config.start_port = 9091
net_config.server_listen_port()
# * The Host option remains unused for now