#!/usr/bin/python
#coding=utf-8
def fun_var_args(farg, *args, **kwargs):  
    print "arg:", farg  
    for value in args:  
        print "another arg:", value  
    print kwargs;
      
fun_var_args(1, "two", 3,  5, "7", "8",  test="33", test2="44", trest33=4444, ) # *args可以当作可容纳多个变量组成的list  

