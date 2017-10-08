#!/usr/bin/python 
#import config
import sys
import os
import re;
pattern=re.compile('.*zip.*');
i=100;
for each in sys.path:
	i=i+1;
	match=pattern.match(each)
	print each;
	if match:
		print "#####",each,i;
