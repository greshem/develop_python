#!/usr/bin/python 
import string
def uppercase_ASCII_string(str):
	newstr = ""
	for i in range(0,len(str)):
		#if str[i] in string.lowercase:
		if str[i] in string.uppercase:
			newstr += chr(ord(str[i])+32)
		else:
			newstr += str[i]

	return newstr

print uppercase_ASCII_string("LINUX");
print uppercase_ASCII_string("LINuX");
