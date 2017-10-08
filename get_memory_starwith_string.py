#!/usr/bin/python

#2011_03_01_11:09:21   ÐÇÆÚ¶þ   add by greshem
import string
import os;
import sys;
def memInstalled():
    f = open("/proc/meminfo", "r")
    lines = f.readlines()
    f.close()
    for l in lines:
        if l.startswith("MemTotal:"):
            fields = string.split(l)
            mem = fields[1]
            break
    return int(mem)

print memInstalled()
