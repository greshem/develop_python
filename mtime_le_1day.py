import os
import time
from os.path import join, getsize


def getMtime(dir):
	#mtime=n;
	i=0;
	cur=time.time();
	for root, dirs, files in os.walk(dir):
		for name in files:
			mtime = os .path.getmtime(join(root,name)) ;
			if (cur-mtime) < 24*60*60:
				print join(root,name);
				#print (cur-mtime);
			else:
				#print (mtime-cur)
				i=i+1;
			#print size

   
#if '__name__' == '__main__':
getMtime('/root')

