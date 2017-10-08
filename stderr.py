#!/usr/bin/python
import sys;
print >> sys.stderr, "timestamp not specified; using the current time"

while 1:
	line=sys.stdin.readline()[:-1]
	print line;

