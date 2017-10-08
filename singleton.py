#!/usr/bin/python
#coding:gbk
#import object;
class   Singleton(object):   #   必须继承object
	number=None;
	def   __new__(cls,   var   ):
		if   cls.number   is   None:
				cls.number   =   object.__new__(cls)
				cls.number.var   =   var
		return   cls.number
a   =   Singleton(5)
b   =   Singleton(6)
print   a.var
print   b.var 
