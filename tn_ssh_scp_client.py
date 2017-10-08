
import sys
import glob
import os

import tn_sshclient
from tn_sshclient import SSHClient

#pip install    ecdsa
#pip install    pycrypto
#pip install    paramiko 

def ssh_execute(client, cmd):
    cmd += " 2>&1"
    print "ssh request: [{0}]".format(cmd)
    stdin, stdout, stderr = client.execute(cmd)
    
    outlines = stdout.readlines()
    if len(outlines) != 0:
        print "ssh response: [{0}]".format("".join(outlines))
    return outlines

def ssh_cp(client, local_path, remote_path):
    print "scp {0} {1}@{2}:{3}".format(local_path, client.user_name, client.ip, remote_path)
    client.put(local_path, remote_path)


if __name__== "__main__": 
    client = sshclient.SSHClient()
    client.connect("192.168.1.11", "root", "Emotibot1")
    lines = ssh_execute(client, "uname -a")
    print lines;

    ssh_cp(client, "/etc/passwd", "/tmp/passwd2222");

