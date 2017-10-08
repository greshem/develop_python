#!/usr/bin/python
#coding:gbk

import commands
import os
import string
import sys
import time
from os.path import join, getsize

import re;

#uname = os.uname()[2]

re_pat=re.compile('todo');
def check_dir(path): 
	for root, dirs, files in os.walk(path):
		for file in files:
			abs_path = os.path.join(root,file)
			#print "%s -> %s" %( file, getsize(abs_path));
			if re_pat.search(file):
				print "%s" %abs_path;
			
			#if long(os.path.basename(abs_path)) != long(getsize(abs_path)):
			#	print "assert ERROR %s"%(abs_path);
			#	sys.exit(-1);


if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = '/etc';

check_dir(path); 


