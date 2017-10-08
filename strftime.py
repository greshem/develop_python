#!/usr/bin/python 
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

import time;
def get_cur_time():
	return time.strftime("%Y-%m-%d_%H:%M:%S ",time.localtime())

    
    

print getTimeStamp();
