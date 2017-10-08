#!/usr/bin/python
#coding:gbk
class Log(object):  
	def __init__():  
		"disable the __init__ method" 

	__inst = None # make it so-called private 
	filehandle=None;
	name = 'myname'

	@staticmethod 
	def getInst():  
		if not Log.__inst:  
			Log.__inst = object.__new__(Log)  
		return Log.__inst

	def SetNameName(self, name = ''):
		if name != '':
			self.name = name

	def GetName(self):
		return self.name

	def SetSetName(self, name = ''):
		if name != '':
			self.name = name

	def Logger(self, str):
		if self.filehandle is None:
			self.filehandle = open("all.log", "w")
		self.filehandle.write("%s\n" % str);

if __name__ =='__main__':
	#print __name__
	Log.getInst().SetSetName("new aaa");
	Log.getInst().SetSetName("new aaa");
	Log.getInst().SetSetName("new aaa");
	Log.getInst().SetNameName("new name");
        
	for i in range(1,100):
		Log.getInst().Logger(" this is logger 第%d次循环"%i);

