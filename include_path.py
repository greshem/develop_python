#!/usr/bin/python 
#import config
import sys
import os
if sys.version_info>(2,5):
	sys.path.append(os.path.join("/root", 'py25modules'));
	print sys.path;
else:
	print("not ok");
	print sys.path;

print("#################################\n");
print sys.path[1:3];
