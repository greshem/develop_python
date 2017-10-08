#!/usr/bin/python 
#coding:gbk
#2011_05_26 by greshem. 
import sys;

print("bbb.py");
if( len(sys.argv) <  2):
   print "Usage:   %s  size "%sys.argv[0];
else:
	print sys.argv;


if sys.platform =='win32':
	print sys.stdin.readline()[:-1];

