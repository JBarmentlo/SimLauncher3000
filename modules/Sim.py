import subprocess
import os
import time
import shlex

class Sim():
    def __init__(self, port, time_till_kill = 600):
        '''
            time_till_kill is in seconds
        '''
        self.port = int(port)
        self.start_time = time.time()
        self.last_ping_time = time.time()
        self.time_till_kill = time_till_kill
        self.process = self.start_sim_proc()


    def start_sim_proc(self):
        cmd = os.environ["SIM_PATH"] + " --port " + str(self.port)
        print(shlex.split(cmd))
        proc = subprocess.Popen(shlex.split(cmd))
        return proc


    def keep_alive_ping(self):
        self.last_ping_time = time.time()

    
    def should_i_be_alive(self):
        if (time.time(0) - self.last_ping_time) > self.time_till_kill:
            return  False
        return True


    def kill_sim(self):
        self.process.kill()

    
    def permapoll(self):
        while True:
            time.sleep(0.3)
            print(self.process.poll())


    def safety_check_port():
        pass
        # TODO: Inquire as to the safety of this

if __name__ == "__main__":
    sim = Sim(8889)
    # sim.permapoll()