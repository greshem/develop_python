#!/usr/bin/python

from BeautifulSoup import BeautifulSoup

file=open("android/1.html").read();
print file;

html = unicode(file,'gb2312','ignore').encode('utf-8','ignore')
content = BeautifulSoup(html).findAll('a')
for item in content:
    print item;


