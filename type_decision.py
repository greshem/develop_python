#!/usr/bin/python 
class objA:
	pass;
A = objA()
B = 'a','v'
C = 'a string'
print isinstance(A, objA)
print isinstance(B, tuple)
print isinstance(C, basestring) 
