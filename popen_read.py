#!/usr/bin/python 
import os;
#string 
a=os.popen("ifconfig -a ").read()
print type(a);
