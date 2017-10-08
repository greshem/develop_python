#-*- coding: UTF-8 -*-
import time
 
def foo():
    time.sleep(2);
    print 'in foo()'
 
# 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
def timeit(func):
    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def greshem():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
     
    # 将包装后的函数返回
    return greshem
 

def  long_line(func):
    def  wrapper():
        print "#================================================";
        func();
        print "#================================================";
    return wrapper;
        
#foo2 = timeit(foo)
#foo2();

long_line(foo)();
