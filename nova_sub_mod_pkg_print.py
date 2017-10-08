#coding=utf-8

import  pkgutil  
def print_nova():
    import nova;
    print "walk_packages %s %s "%(nova.__path__,  nova.__name__+".");
    for each in pkgutil.walk_packages(nova.__path__,  nova.__name__+"."):
        print each;


#字符串的方式打印
def print_nova_with_str():
    for each in pkgutil.walk_packages ('/usr/lib/python2.7/site-packages/nova',  "nova."):
        print each; 

print_nova_with_str();

