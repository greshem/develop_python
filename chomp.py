#!/usr/bin/python 
def chomp(line):
	if line[-1] == '\n':
		line = line[:-1]
	return line;


fh=open("/etc/passwd");
for line in fh.readlines():
    print chomp(line);

