#coding=utf-8
#无参数装饰器 C 包装带参数函数
def decorator_func_args(func):
    def handle_args(*args, **kwargs): #处理传入函数的参数
        print "begin"
        func(*args, **kwargs)   #函数调用
        print "end"
    return handle_args


@decorator_func_args
def foo2(a, b=2,c=3):
    print a, b,c

foo2(1,3,4)
