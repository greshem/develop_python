#!/usr/bin/python
import re;
char = re.compile("port.*=.*#.*")
f=open("/root/bin/daemon/ssh_nat/ssh_phabricator.pl", "r");
lines=f.readlines();
#print lines;

#output= [ re.findall(char, item)[0]  for item in lines if re.search(char, item)]
#print output;

for item in lines:
    if re.search(char, item):
        #print item;
        print re.findall(char,item)[0];
