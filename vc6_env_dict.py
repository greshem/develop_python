#!/usr/bin/python

#2011_02_11_12:35:02 add by greshem
data={
		"C:\Program Files\Microsoft Visual Studio\VC98\atl\include":"INCLUDE",
		"C:\Program Files\Microsoft Visual Studio\VC98\mfc\include":"INCLUDE",
		"C:\Program Files\Microsoft Visual Studio\VC98\include":"INCLUDE",
		
		"C:\Program Files\Microsoft Visual Studio\VC98\mfc\lib":"LIB",
		"C:\Program Files\Microsoft Visual Studio\VC98\lib":"LIB", 

		"C:\Program Files\Microsoft Visual Studio\Common\Tools\WinNT":"PATH",
		"C:\Program Files\Microsoft Visual Studio\Common\MSDev98\Bin":"PATH",
		"C:\Program Files\Microsoft Visual Studio\Common\Tools":"PATH",
		"C:\Program Files\Microsoft Visual Studio\VC98\bin":"PATH",
		
		};

env={};
for key in data.keys():
	value=data[key];
	print "%s --> %s" %(key, value);
	if not env.has_key(value) :
		env[value]=key;
	else:
		tmp=("%s;%s")% (env[value], key);
		env[value]=tmp;

for key in env.keys():
	print "%s --> %s" %(key, env[key]);
