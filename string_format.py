#!/usr/bin/python
import glob
import os;
for file in glob.glob("*"):
	#if os.path.isfile(file):
    if os.path.isdir(file):
        print(file)
    elif os.path.isfile(file):
        print "File:   {0}".format(file);
