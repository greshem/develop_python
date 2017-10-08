#!/usr/bin/python
#bs=b"3333";
bs="3333";
file=open("/etc/passwd", 'r');
tmp=file.read(len(bs))
print "tmp",tmp
if file.read(len(bs)) == "root":
	print "ok"
else:
	print "not ok"
file.close();
