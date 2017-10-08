#!/usr/bin/python
#2011_01_12_16:06:40 add by greshem
#chomp 的问题没有解决. 
import random
fh=open("/etc/passwd");
lines=fh.readlines();
#print lines

random.shuffle(lines);
for line in lines:
	print line

