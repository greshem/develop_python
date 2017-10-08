#!/usr/bin/python
import sys;
import time;

def getTimeStamp():
	"""
	Method to get a timestamp to be used in
	the log message.
	Args:
	  None

	Returns: [STRING] The timestamp
	"""

	#return time.strftime("%m.%d.%y %H:%M:%S ",time.localtime())
	return time.strftime("%Y-%m-%d_%H:%M:%S ",time.localtime())


def  save_argc_string():
	f = open("/var/log/yum.log", "a+")
	today=getTimeStamp()
	f.write("\n#%s\n"%(today));

	for arg in sys.argv:
	    f.write("%s\n"%(arg));
	    f.close();#bug should close it.


save_argc_string();



