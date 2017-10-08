#coding:gbk 
#!/usr/bin/python
import re;
root_pat=re.compile('root');

fh=open("/etc/passwd");
for line in fh.readlines(): 
	#match=root_pat.match(line)
	match=root_pat.search(line)
	if match: 
		print line


root_pat=re.compile('^\[');
match=root_pat.search("[adfafasasf");
print match

