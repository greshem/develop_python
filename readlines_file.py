#!/usr/bin/python
fh=open("/etc/passwd");
for line in fh.readlines():
	print line
	for tmp in line.split(':'):
		print tmp

