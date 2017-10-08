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



#2011_02_11_14:52:34 add by greshem
if not data.has_key("wenwen"):
	data['wenwen']="qianyicheng";


print data;
