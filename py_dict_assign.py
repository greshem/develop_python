#!/usr/bin/python
#2011_01_12_16:28:21 add by greshem
import re
import sys

next = {}
next['if'] = next['elif'] = 'elif', 'else', 'end'
next['while'] = next['for'] = 'else', 'end'
next['try'] = 'except', 'finally'
next['except'] = 'except', 'else', 'finally', 'end'
next['else'] = next['finally'] = next['def'] = next['class'] = 'end'
next['end'] = ()
start = 'if', 'while', 'for', 'try', 'with', 'def', 'class'

print next;
print next.keys();
print next['if'];
del next['if'];
print next.items();

for v,k in next:
	print v,"->",k;
