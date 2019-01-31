import pexpect
import time
import os
import sys

env = dict(os.environ); 
env["LOGNAME"]='demo_machine'
env['TERM']='xterm-256color'
env["USER"]="demo_machine"

if len(sys.argv)<2:
    print("Usage: ./typer examples/scenario.sh")
else:
    scenario = sys.argv[1]

child = pexpect.spawn('./cinemaizer.sh %s.cast'%(scenario), env = env)
time.sleep(0.5)
fh = open(scenario)
for line in fh:
    if line.startswith('#expect:'):
        print("Yay expecting")
    elif line.startswith('#wait:'):
        pass
    elif line.startswith('#send-ctrl:'):
        pass
    elif line.startswith('#send:'):
        pass
    elif line.startswith('#'):
        pass
    else:
        for char in line:
            time.sleep(0.1)
            child.send(char)
    child.expect("demo_machine")
fh.close()
time.sleep(1)

