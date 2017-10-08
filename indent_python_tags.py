#!/usr/bin/python 
#coding:gbk
#2011_06_15 by greshem. 
import sys;
bakefile_tag_start="<bakefile>"
bakefile_tag_end="</bakefile>"

middle_tag_start="<middle>";
middle_tag_end="</middle>";


i=bakefile_tag_start +"\n"\
+     	middle_tag_start+"\n"\
+		middle_tag_end+"\n"\
+bakefile_tag_end;	
print i
