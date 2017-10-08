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

re_pat=re.compile('.*todo.*');

def chomp(line):
    if line[-1] == '\n':
        line = line[:-1]
    return line;

def check_dir(path): 
	for root, dirs, files in os.walk(path):
		for file in files:
			abs_path = os.path.join(root,file)
			#print "%s -> %s" %( file, getsize(abs_path));
			#if re_pat.search(file):
			if re_pat.match(file):
				print "#################################################";
				print "%s" %abs_path;
				print_file_not_comment(abs_path);
			
			#if long(os.path.basename(abs_path)) != long(getsize(abs_path)):
			#	print "assert ERROR %s"%(abs_path);
			#	sys.exit(-1);

def print_file_not_comment(abs_path):
	line_pattern=re.compile('^#');	
	fh=open(abs_path);
	for line in fh.readlines():
		if not line_pattern.match(line):
			print "%s"% chomp(line);	

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = './';

check_dir(path); 


