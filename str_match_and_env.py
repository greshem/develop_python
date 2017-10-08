
import os
import re

print 'C:\\Program Files\\WinRAR\\WinRar.exe'
if not os.path.exists("test4.py") and not 0:
	print "There is no gtest.zip"

dll = re.compile(r'\bC:\\Bakefile\b')
pathlist=os.environ['PATH'].split(os.pathsep)
for path in pathlist:
	if dll.search(path):
		print path
	if len(path)==0:
		print "eof"

def test():
	find="112222"
	return find

print test()

def check_env():
	bake = re.compile(r'\bC:\\Bakefile\b')
	vc2003 = re.compile(r'\bD:\\Microsoft Visual Studio .NET 2003\\Vc7\\bin\b')
	pathlist=os.environ['PATH'].split(os.pathsep)
	find_bake=0
	find_vc2003=0
	for path in pathlist:
		print path
		if bake.search(path):
			find_bake=1
		if vc2003.search(path):
			find_vc2003=1
	if 1==find_bake and 1==find_vc2003:
		return 1
	else:
		return 0
			
print check_env()