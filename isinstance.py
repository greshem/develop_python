#!/usr/bin/python
# �ж��Ƿ��Ǽ̳й�ϵ. 
import  xmlparser
def check(desc):
    if isinstance(desc, xmlparser.Element):
		print "ok"
    else:
		print "not ok"
a="333";
check(a);
