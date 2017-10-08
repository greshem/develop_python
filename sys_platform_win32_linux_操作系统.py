import os;
import sys;
import string;
#2011_01_22_01:42:48 add by greshem
#tell the os version
if sys.platform =='win32':
	print "i am win32";
elif sys.platform =='mac':
	print "i am mac";
elif sys.platform.startswith("linux"):
	print "i am linux";
else:
	print "other os";


