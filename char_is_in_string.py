#!/usr/bin/python 

whitespace = ' \t\n\r\v\f'    
lowercase = 'abcdefghijklmnopqrstuvwxyz' 
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
letters = lowercase + uppercase
ascii_lowercase = lowercase   
ascii_uppercase = uppercase   
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'         
hexdigits = digits + 'abcdef' + 'ABCDEF' 
octdigits = '01234567'        
punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + letters + punctuation + whitespace

if 'a' in lowercase:
	print "ok"
if '#' in punctuation:
	print "ok"
