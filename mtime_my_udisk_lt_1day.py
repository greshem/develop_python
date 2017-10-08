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
	print path;
	if os.path.isdir(path):
		return 1;

	path="%s:/%s"%(disk_char,"oss_site_all_iso");
	print path;
	if os.path.isdir(path):
		return 1;

	path="%s:/%s"%(disk_char,"photo");
	print path;
	if os.path.isdir(path):
		return 1;

	path="%s:/%s"%(disk_char,"_work_and_todo_keyword");
	print path;
	if os.path.isdir(path):
		return path;

	return 0;	

##################mainloop 
path="c:/bb/dd";
for i  in range(0,26):
	path=increate_windows_disk(path);
	print is_qzj_work_disk(path);
