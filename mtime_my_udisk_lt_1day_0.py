#!/usr/bin/python 
#20110120 greshem
import os;
import string

def get_disk_char(str):
	disk_char=str[0:1]
	return disk_char;

def increate_windows_disk(str):
	newstr=""
	for i in range(0,len(str)):
		if i==0 :
			newstr = chr(ord(str[0])+1)
		else:
			newstr+=str[i];

	return newstr

def is_qzj_work_disk(path):
	#my _pre_cache
	disk_char=get_disk_char(path);
	path="%s:/%s"%(disk_char,"_pre_cache");
	path1="%s:/%s"%(disk_char,"all_chm");
	#print path;
	if os.path.isdir(path) and os.path.isdir(path1) :
		return "sdb1";

	path="%s:/%s"%(disk_char,"oss_site_all_iso");
	path1="%s:/%s"%(disk_char,"linux_src_all_iso");
	#print path;
	if os.path.isdir(path) and os.path.isdir(path1):
		return "sdb2";

	path="%s:/%s"%(disk_char,"photo");
	path1="%s:/%s"%(disk_char,"develop_IDE_ISO");
	#print path;
	if os.path.isdir(path) and os.path.isdir(path1):
		return "sdb3";

	path="%s:/%s"%(disk_char,"_work_and_todo_keyword");
	path1="%s:/%s"%(disk_char,"my_usb_video_driver");
	#print path;
	if os.path.isdir(path) and os.path.isdir(path1):
		return "sdb4";

	return 0;	

##################mainloop 
path="c:/bb/dd";
for i  in range(0,26):
	path=increate_windows_disk(path);
	label=is_qzj_work_disk(path);
	if  label=="sdb1" :
		print "sdb1 is %s" %(path);
	elif label=="sdb2" :
		print "sdb2 is %s" %(path);
	elif label=="sdb3" :
		print "sdb3 is %s" %(path);

	elif label=="sdb4" :
		print "sdb4 is %s" %(path);
	else:
		print " %s is no qzj_disk " %(path);


print "END\n";
