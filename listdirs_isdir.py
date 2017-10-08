import os;
import sys;
for pkg in  os.listdir("/etc/"):
	d="/etc/%s"%pkg;
	if not os.path.isdir(d):
		print  "FILE %s"%d;


	

