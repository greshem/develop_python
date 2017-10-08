#!/usr/bin/python
# 判断是否是继承关系. 
import  xmlparser
def check(desc):
    if isinstance(desc, xmlparser.Element):
		print "ok"
    else:
		print "not ok"
a="333";
check(a);
