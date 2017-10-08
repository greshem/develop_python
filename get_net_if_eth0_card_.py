#!/usr/bin/python 
import psutil

a=psutil.net_if_stats()
print a;
print type(a);
print a.keys();

