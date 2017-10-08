

def function_wrapper2(wrapped):
    print '==========================='
    def _wrapper(*args, **kwargs):
        return wrapped(*args, **kwargs)
    return _wrapper 

def function_wrapper(wrapped):
    print '###########################'
    def _wrapper(*args, **kwargs):
        return wrapped(*args, **kwargs)
    return _wrapper 

print type(function_wrapper);

@function_wrapper
@function_wrapper2
def fun_var_args(farg,name=333, last=3333,  *args,  **kwargs  ):  
    print "arg:", farg  
    print "name:%s"%name;
    print "last:%s"%last;
    print args;
    print kwargs;

fun_var_args(1, 44444, 55555, 66666,test="33", test2="444");

  
