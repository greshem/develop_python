#!/usr/bin/python
#coding:gbk

import commands
import os
import string
import sys
import time
from os.path import join, getsize


#uname = os.uname()[2]

def cmp_with_mtime(a,b):
	a_mtime = os.path.getmtime(a) ;
	b_mtime = os.path.getmtime(b) ;
	return cmp(b_mtime, a_mtime);

def get_dir_list(path): 
	filelist=[];
	for root, dirs, files in os.walk(path):
		for file in files:
			abs_path = os.path.join(root,file)
			#print "%s" %abs_path;
			if os.path.isfile(abs_path):
				filelist.append(abs_path);
	
	return filelist;
			
			

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = './';


list=get_dir_list(path);

list.sort( cmp_with_mtime);
#for i in list:
print list[0:10];

if sys.platform =='win32':
	print sys.stdin.readline()[:-1];


