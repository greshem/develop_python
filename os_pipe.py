#code from  commands.py  getoutput 

import os
#pipe = os.popen('{  ifconfig ; } 2>&1', 'r')
pipe = os.popen('cat /etc/passwd ', 'r')
#for each in pipe.readlines():
for each in pipe:
    print each,
#text = pipe.read()
#sts = pipe.close()

