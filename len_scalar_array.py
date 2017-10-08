#!/usr/bin/python
#2011_01_12_17:02:40 add by greshem
import sys;
def wc(fn):
	try:
		f=open(fn,'rt');
		cnt=len(f.readlines());
		f.close();
		return cnt;
	except IOError:
		return 0;

for arg in sys.argv:
	print arg,"\t"
	print wc(arg);
