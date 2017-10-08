import libvirt
import re

#import sys
#import os
#import libxml2
#import pdb



def list_network():
    nums=[];
    conn = libvirt.openReadOnly(None)
    if conn is None:
        print('Failed to open connection to the hypervisor')
        sys.exit(1)

    for each in conn.listAllNetworks():
        print each.name();

list_network();

