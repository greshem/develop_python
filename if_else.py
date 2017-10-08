import sys,os.path

#2011_02_11_11:17:19 add by greshem
#if 0:
if 0:
	print("ok");
else:
	print("not ok");

#用 多个if 代替  if else if; else if; else; 
# 
if fetch == 'wget':
	fetch_cmd = 'wget %s -O /dev/null --quiet --tries=1' % (url)
if fetch == 'fetch':
	fetch_cmd = 'fetch -o /dev/null -q %s' % (url)
if fetch == 'curl':
	fetch_cmd = 'curl -o /dev/null -s --retry 1' % (url)

