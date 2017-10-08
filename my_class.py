#!/usr/bin/python

class Person:
    def __init__(self,name):
        self.name=name
    def sayhello(self):
        print 'My name is:',self.name

p=Person('tianya')
p=Person('wenshuna')
p.sayhello();
#print p
