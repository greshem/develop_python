#!/usr/bin/python
#2011_01_12_16:06:40 add by greshem
#chomp ������û�н��. 
import random
fh=open("/etc/passwd");
lines=fh.readlines();
#print lines

random.shuffle(lines);
for line in lines:
	print line

