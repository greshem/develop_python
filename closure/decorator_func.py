#coding=utf-8


def thin_line(func):
    def wrapper(*args, **kwargs):
        print  "#---------------------------------";
        return func(*args, **kwargs)
    return wrapper


def middle_line(func):
    def wrapper(*args, **kwargs):
        print  "#==================================";
        return func(*args, **kwargs)
    return wrapper


def bold_line(func):
    def wrapper(*args, **kwargs):
        print  "##################################";
        return func(*args, **kwargs)
    return wrapper

@bold_line
@middle_line
@thin_line
def func(name):
    print 'my name is', name

#@thin_line
def func2(name):
    print 'my name is', name


#func("test");

#等同如下:
bb=middle_line(bold_line(thin_line(func2)));
bb("aaa")


func("cccccccccc");
