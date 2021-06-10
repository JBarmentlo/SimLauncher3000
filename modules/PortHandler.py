from config import simconfig

# TODO: check for port conflicts with PrivateAPI port

class PortHandler():
    def __init__(self, start_port = 9090, nb_ports = simconfig.max_concurrent_sims):
        '''
            An object for handling ports.
            self.status[9090] == True means the port 9090 is available.

        Args:
            start_port (int, optional): [description]. Defaults to 9090.
            nb_ports ([type], optional): [description]. Defaults to simconfig.max_concurrent_sims.
        '''
        self.status = self.create_status(start_port, nb_ports)


    def create_status(self, start_port, nb_ports):
        status = {}
        for i in range(nb_ports):
            status[i] = True
        return status

    
    def is_port_availabe(self, port_no):
        '''
            Returns True is port_no is available and within the allowed range

        Args:
            port_no ([int]): requested port number

        Returns:
            [bool]: Availability
        '''
        try:
            return (self.status[port_no])
        except:
            return False

    
    def get_port_no(self):
        '''
            Returns:
                int: Available port, None if no port is available
        '''
        for key, value in self.status:
            if (value):
                return(key)
        return(None)