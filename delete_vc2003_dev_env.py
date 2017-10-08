#coding:gbk
#vc6 的所有的 注册表的东西都集中在    HKEY_CURRENT_USER\Environment 下
#HKEY_CURRENT_USER\Environment\lib
#HKEY_CURRENT_USER\Environment\include
#HKEY_CURRENT_USER\Environment\path

import sys
import site
import os
import _winreg

HKCU = _winreg.HKEY_CURRENT_USER
ENV = "Environment"
PATH = "PATH"
LIB = "LIB"
INCLUDE = "INCLUDE"
DEFAULT = u"%PATH%"

def modify_evn_lib():
    with _winreg.CreateKey(HKCU, ENV) as key:

	pass;
	
def modify_evn_include():
	pass;
	
def modify_env(path):
	#with 的用法， 用来生成一个对象. 
    with _winreg.CreateKey(HKCU, ENV) as key:
        try:
            envpath = _winreg.QueryValueEx(key, path)[0]
        except WindowsError:
            envpath = DEFAULT
        paths=[envpath];
        rets=[];
        array=envpath.split(";");
        for each in array:
			if not "2003\\" in each:
				rets.append(each);
			else:
			    print "%s delete "%each;
			
        envpath = os.pathsep.join(rets)
        print  "DDD:%s"%envpath;
        _winreg.SetValueEx(key, path, 0, _winreg.REG_EXPAND_SZ, envpath)
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
    main(PATH)
    main(LIB)
    main(INCLUDE)
