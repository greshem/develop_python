#!/usr/bin/python

import commands
import os
import string
import sys
from os.path import join, getsize


uname = os.uname()[2]

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = './tmp';
    
for root, dirs, files in os.walk(path):
	for file in files:
		abs_path = os.path.join(root,file)
		#print "%s -> %s" %( file, getsize(abs_path));
		
		if long(os.path.basename(abs_path)) != long(getsize(abs_path)):
			print "assert ERROR %s\n"%(abs_path);
			#sys.exit(-1);


print "########################################################################";
print "ok, check success \n";



