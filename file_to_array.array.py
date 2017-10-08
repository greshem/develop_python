import os;
output=os.popen("ifconfig");
ifcfg= output.readlines();
array=[ line.lower().split() for line in ifcfg ]
print array;
