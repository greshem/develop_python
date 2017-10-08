# -*- coding: utf-8 -*-
import inspect
#Qdef a(a, b=0, *c, d, e=1, **f):
def a(a, **f):
    pass
aa = inspect.signature(a)
print("inspect.signature（fn)是:%s" % aa)
print("inspect.signature（fn)的类型：%s" % (type(aa)))
print("\n")
