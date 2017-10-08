
def deco_functionNeedDoc(func):
    if func.__doc__ == None :
        print func, "has no __doc__, it's a bad habit."
    else:
        print func, ':', func.__doc__, '.'
    return func

@deco_functionNeedDoc
def f():
    print 'f() Do something'

@deco_functionNeedDoc
def g():
    '''I have a __doc__'''
    print 'g() Do something'

f()
g()

