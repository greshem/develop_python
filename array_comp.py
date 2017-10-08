#!/usr/bin/python
import sys
if sys.version_info[0:3] < (2,3,0):
	sys.stderr.write('error: requires at leasst Python 2.3.0');
	sys.exit(1);
else:
	sys.stdout.write('version check ok');
