#!/usr/bin/python 
#coding:gbk
#2011_01_27_18:42:44 add by greshem, 
import time;
import os;
import sys;
def gen_file_name_with_time(prefix, suffix):
	i=1;
	cur_time=time.strftime("%Y_%m_%d",time.localtime())
	while i:
		filename="%s_%s_%d.%s"%(prefix,cur_time,i,suffix);
		i=i+1;
		if not os.path.isfile(filename):
			return filename;	

def touch_file(filename):
	fh=open(filename,"wb");
	fh.write("%s"%filename);
	fh.close();

def must_be_exist(filename):
	if not os.path.isfile(filename):
		print "%s ASSERT ERROR"%filename;
		os.exit(-1);


for i in range(0,100):
	name=gen_file_name_with_time("back","zip");
	print name;
	touch_file(name);
	must_be_exist(name);	
	

