#!/usr/bin/python
import os,sys,string
import getopt
import time

data = {"timestamp": None,
        "releasestr": None};
print data;
print "###############################################################################"
if data["timestamp"] is None:
    print >> sys.stderr, "timestamp not specified; using the current time"
    data["timestamp"] = time.time()

print data;
