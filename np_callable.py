#!/usr/bin/python
import numpy as np;
import numpy ;
from  types import *;


def dump_function(module_str):
    
    
    #a=__import__("np.%s"%each);
    a=eval("%s"%module_str);
    #print type(a);
    #if  type(a) ==  ModuleType:
    if not isinstance(a, ModuleType):
        print "%s is not module %s "%(module_str, type(a));
        return ;

    #print dir(a);
    for each in  dir(a):
        sub_module_str="%s.%s"%(module_str, each);
        if each.startswith("_"):
            continue;
        #print "GGG: %s" %sub_module_str;
        b=eval(sub_module_str);
        if callable(b):
            continue;
            pass;
            #print "========================";
            print "%s  is funcion "%each;
            #print a.__doc__;
        

        #if type(b)=="module":
        if  type(b) ==  ModuleType:
            print "import %s"%sub_module_str;
            try:
                __import__(sub_module_str);
            except Exception as e:
                print "import ERROR; %s"%e;
                #return; 

            print "sub_module %s" %(sub_module_str);
            dump_function(sub_module_str);
            

dump_function("numpy");
#dump_function("np");
#print dir(numpy);
#print dir(np);
