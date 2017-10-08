# modules_functions.py 
def describe_func(obj, method=False):
   """ Describe the function object passed as argument.
   If this is a method object, the second argument will
   be passed as True """
    
   if method:
      wi('+Method: %s' % obj.__name__)
   else:
      wi('+Function: %s' % obj.__name__)
 
   try:
       arginfo = inspect.getargspec(obj)
   except TypeError:
      print
      return
    
   args = arginfo[0]
   argsvar = arginfo[1]
 
   if args:
       if args[0] == 'self':
           wi('\t%s is an instance method' % obj.__name__)
           args.pop(0)
 
       wi('\t-Method Arguments:', args)
 
       if arginfo[3]:
           dl = len(arginfo[3])
           al = len(args)
           defargs = args[al-dl:al]
           wi('\t--Default arguments:',zip(defargs, arginfo[3]))
 
   if arginfo[1]:
       wi('\t-Positional Args Param: %s' % arginfo[1])
   if arginfo[2]:
       wi('\t-Keyword Args Param: %s' % arginfo[2])

