#!/usr/bin/python
#coding=utf-8
import sys;

def fun_var_args(farg, input2, *args,  **kwargs  ): 
    print "farg:", farg  
    print "input2:", input2
    for value in args:  
        print "another arg:", value  
    print kwargs;
    sub_net = kwargs.get('subnet', None)
    if sub_net == None:
        print "sub_net  in  kwargs is none ";
        #sys.exit(-1);
            

def test_kwargs(farg, input2,   **kwargs  ): 

    print "#=================================\n";
    print kwargs;
    sub_net = kwargs.get('subnet', None)
    if sub_net == None:
        print "sub_net  in  kwargs is none ";
        sys.exit(-1);
      
fun_var_args(1, "two", 3,  5, "7", "8",  test="33", test2="44", trest33=4444, ) # *args可以当作可容纳多个变量组成的list  

test_kwargs("farg",  "dfasfasfasf",  subnet="33333", subnet2="4444");
