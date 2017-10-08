#coding:gbk 
#!/usr/bin/python
#
#2011_01_11_17:20:53 add by greshem
import re;
#root_pat=re.compile('root');
root_pat=re.compile('root');

fh=open("/etc/passwd");
#注意 fh.readlines readline 的区别. 
#for line in fh.readline():
for line in fh.readlines():
	#print line;
	match=root_pat.match(line)
	#match=root_pat.search(line)
	if match: 
        print "GGGG%s"%(match);
        print line

