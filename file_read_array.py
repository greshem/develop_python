#!/usr/bin/python

all_the_text = open('/etc/passwd').read( )     # 
print all_the_text;

fh=open("/etc/passwd");
for line in fh.readlines(): 
	print line
fh.close();


fh=open("/etc/passwd");
array=fh.readlines();
print array;
fh.close();


