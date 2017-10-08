#!/usr/bin/python
#coding=utf-8
#closure;

#这里面调用func的时候就产生了一个闭包——inner_func,并且该闭包持有自由变量——name，因此这也意味着，当函数func的生命周期结束之后，name这个变量依然存在，因为它被闭包引用了，所以不会被回收。
#另外再说一点，闭包并不是Python中特有的概念，所有把函数做为一等公民的语言均有闭包的概念。不过像Java这样以class为一等公民的语言中也可以使用闭包，只是它得用类或接口来实现。
#更多概念上的东西可以参考最后的参考链接。

def func(name):
        def inner_func(age):
            print 'name:', name, 'age:', age
        return inner_func

@func(33)
def  test():
    print "fffff"; 

bb = func('greshem')
bb(35)  # >>> name: the5fire age: 26

test();
