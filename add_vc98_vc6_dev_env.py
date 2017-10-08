#coding:gbk
#vc6 的所有的 注册表的东西都集中在    HKEY_CURRENT_USER\Environment 下
#HKEY_CURRENT_USER\Environment\lib
#HKEY_CURRENT_USER\Environment\include
#HKEY_CURRENT_USER\Environment\path

import sys
import site
import os
import _winreg

data={
		"C:\Program Files\Microsoft Visual Studio\VC98\atl\include":"INCLUDE",
		"C:\Program Files\Microsoft Visual Studio\VC98\mfc\include":"INCLUDE",
		"C:\Program Files\Microsoft Visual Studio\VC98\include":"INCLUDE",
		
		"C:\Program Files\Microsoft Visual Studio\VC98\mfc\lib":"LIB",
		"C:\Program Files\Microsoft Visual Studio\VC98\lib":"LIB", 

		"C:\Program Files\Microsoft Visual Studio\Common\Tools\WinNT":"PATH",
		"C:\Program Files\Microsoft Visual Studio\Common\MSDev98\Bin":"PATH",
		"C:\Program Files\Microsoft Visual Studio\Common\Tools":"PATH",
		"C:\Program Files\Microsoft Visual Studio\VC98\\bin":"PATH",
		
		};

HKCU = _winreg.HKEY_CURRENT_USER
ENV = "Environment"
PATH = "PATH"
LIB = "LIB"
INCLUDE = "INCLUDE"
DEFAULT = u"%PATH%"

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
		

	
def modify_env(path):
	#with 的用法， 用来生成一个对象. 
    with _winreg.CreateKey(HKCU, ENV) as key:
        try:
            envpath = _winreg.QueryValueEx(key, path)[0]
        except WindowsError:
            print "queryValueEx error"
            envpath = DEFAULT
		
        rets=[envpath];
        paths=[envpath];
        if not "Studio\\" in envpath:
            rets.append(env[path]);
        else:
            print "vc6 have add ";
			
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
    paths, envpath = modify_env(path)
    if len(paths) > 1:
        print "Path(s) added:"
        print '\n'.join(paths[1:])
    else:
        print "No path was added"
    print "\nPATH is now:\n%s\n" % envpath
    expand_path(envpath);

if __name__ == '__main__':
    env=change_to_register_pattern(data);
    main(PATH)
    main(LIB)
    main(INCLUDE)
