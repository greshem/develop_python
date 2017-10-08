#coding:gbk
#2011_02_11_ add by greshem
#HKEY_CURRENT_USER\Environment\lib
#HKEY_CURRENT_USER\Environment\include
#HKEY_CURRENT_USER\Environment\path

import sys
import site
import os
import _winreg


#2011_02_11_17:49:39 add by greshem
#选用了这样的数据库的方式 实用的时候 需要转换一下，  后面的 INCLUDE LIB PATH 作为 key. 
#这样的方式其实便于添加新的路径. 
data={

		"C:\Program Files\Microsoft Visual Studio .NET 2003\SDK\\v1.1\include":"INCLUDE",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\VC7\ATLMFC\INCLUDE": "INCLUDE",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\VC7\INCLUDE": "INCLUDE",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\VC7\PlatformSDK\include": "INCLUDE",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\VC7\PlatformSDK\include\prerelease": "INCLUDE",

		

		"C:\Program Files\Microsoft Visual Studio .NET 2003\SDK\\v1.1\Lib":"LIB",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\SDK\\v1.1\lib": "LIB",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\VC7\ATLMFC\LIB": "LIB",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\VC7\LIB": "LIB",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\VC7\PlatformSDK\lib": "LIB",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\VC7\PlatformSDK\lib\prerelease": "LIB",

	

		"C:\Program Files\Microsoft Visual Studio .NET 2003\Common7\IDE":"PATH",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\Common7\Tools" :"PATH",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\Common7\Tools\\bin" :"PATH",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\Common7\Tools\\bin\prerelease" :"PATH",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\SDK\\v1.1\\bin" :"PATH",
		"C:\Program Files\Microsoft Visual Studio .NET 2003\VC7\\BIN" :"PATH",
		
		};

HKCU = _winreg.HKEY_CURRENT_USER
########################################################################
MAIN_KEY = "Environment"

########################################################################
SUB_KEY1_PATH = "PATH"
SUB_KEY2_LIB = "LIB"
SUB_KEY3_INCLUDE = "INCLUDE"
SUB_KEY4_DEFAULT = u"%PATH%"

env={};

def change_to_register_pattern(data):
	env={};
	for key in data.keys():
		value=data[key];
		print "%s --> %s" %(key, value);
		if not env.has_key(value) :
			env[value]=key;
		else:
			tmp=("%s;%s")% (env[value], key);
			env[value]=tmp;

	#for key in env.keys():
	#	print "%s --> %s" %(key, env[key]);
	return env;
		

	
def modify_main_key(path):
	#with 的用法， 用来生成一个对象. 
	#从HKEY_CURRENT_USER/Environment/$path 下获取 string1;string2;string3的字符串. 
	#假如不再存 2003 字符串 就添加 vc2003_str1;vc2003_str2;vc2003_str3 这样的字符串.  

    with _winreg.CreateKey(HKCU, MAIN_KEY) as key:
        try:
            envpath = _winreg.QueryValueEx(key, path)[0]
        except WindowsError:
            print "queryValueEx error"
            envpath = DEFAULT
		
        rets=[envpath];
        paths=[envpath];
        if not "2003\\" in envpath:
            rets.append(env[path]);
        else:
            print "##vc2003 have add ";
			
        reg_string = os.pathsep.join(rets)
        print  "DDD:%s"%reg_string;
        _winreg.SetValueEx(key, path, 0, _winreg.REG_EXPAND_SZ, reg_string)
        return paths, envpath

def expand_path(envpath):
    print "Expanded:"
    all=_winreg.ExpandEnvironmentStrings(envpath)
    array=all.split(";");
    array.sort();
    for key in array:
		print key;    
        
        
        
        
def main(path):
    paths, envpath = modify_main_key(path)
    if len(paths) > 1:
        print "Path(s) added:"
        print '\n'.join(paths[1:])
    else:
        print "No path was added"
    print "\nPATH is now:\n%s\n" % envpath
    expand_path(envpath);

if __name__ == '__main__':
    env=change_to_register_pattern(data);
	# SUB_KEY1_PATH = "PATH"
	# SUB_KEY2_LIB = "LIB"
	# SUB_KEY3_INCLUDE = "INCLUDE"
	# SUB_KEY4_DEFAULT = u"%PATH%"
    main(PATH)
