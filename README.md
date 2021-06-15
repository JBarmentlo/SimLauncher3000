# SimLauncher3000
Launch Donkey Car Simulation.

launch the server :    
```python srcs/servermain.py```

Use the client   
```python
from modules import Client

c = Client()
c.request_simulator()
c.ping_sim()
c.kill_sim()
```
