#!/usr/bin/python
#coding:gbk 
#
#2011_01_11_17:20:53 add by greshem
import re;
import os;
import time;
#root_pat=re.compile('root');

def get_cpu_usage():
	root_pat=re.compile('^cpu');
	fh=open("/proc/stat");
	for line in fh.readlines():
		match=root_pat.match(line)
		if match: 
			break;

	stats=line.split();
	total=int(stats[1]) + int(stats[2])+int(stats[3]) +int(stats[4]);
	idle=stats[4];
		# 返回当前 CPU 的 total 和 idle 时间片计数 
	return (total, idle);

while 1:
	total1,idle1=get_cpu_usage();
	time.sleep(5);
	total2,idle2=get_cpu_usage();

	total=int(int(total2)-int(total1));
	idle= int(int(idle2) -int(idle1));

	print "total  ",total, "idle ", idle;
	per = 100*(total -idle ) /total;
	print "cpu占用率", per;
	os.system("free ");
	print "###############################";



