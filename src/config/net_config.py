from utils import DotDict

net_config = DotDict()
net_config.host = 'localhost'
net_config.start_port = 9091

net_config.server_port = 9089
net_config.server_refresh_time = 1 # seconds to wait before listening again

net_config.start_sim_request = "start sim"
net_config.stop_sim_request = "stop sim"
net_config.ping_request = "ping"

# * The Host option remains unused for now