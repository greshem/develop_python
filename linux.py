#!/usr/bin/python 
#coding:gbk
#2011_01_27 by greshem. 
import sys;

print("linux.py");
if( len(sys.argv) <  2):
   print "Usage:   %s  size "%sys.argv[0];
else:
	print sys.argv;


if sys.platform =='win32':
	print sys.stdin.readline()[:-1];

