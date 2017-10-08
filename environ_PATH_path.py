#!/usr/bin/python
import os;
pathlist=os.environ['PATH'].split(os.pathsep)
for path in pathlist:
	print path;

