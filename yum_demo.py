#!/usr/bin/python
import sys
import time;



def getTimeStamp():
	"""
	Method to get a timestamp to be used in
	the log message.
	Args:
	  None

	Returns: [STRING] The timestamp
	"""

	#return time.strftime("%m.%d.%y %H:%M:%S ",time.localtime())
	return time.strftime("%Y-%m-%d_%H:%M:%S ",time.localtime())


def  save_argc_string():
	f = open("/var/log/yum.log", "a+")
	today=getTimeStamp()
	f.write("\n#%s\n"%(today));

	for arg in sys.argv:
	    f.write("%s\n"%(arg));
        f.close();


save_argc_string();






try:
    import yum
except ImportError:
    print >> sys.stderr, """\
There was a problem importing one of the Python modules
required to run yum. The error leading to this problem was:

   %s

Please install a package which provides this module, or
verify that the module is installed correctly.

It's possible that the above module doesn't match the
current version of Python, which is:
%s

If you cannot solve this problem yourself, please go to 
the yum faq at:
  http://yum.baseurl.org/wiki/Faq
  
""" % (sys.exc_value, sys.version)
    sys.exit(1)

sys.path.insert(0, '/usr/share/yum-cli')
try:
    import yummain
    yummain.user_main(sys.argv[1:], exit_code=True)
except KeyboardInterrupt, e:
    print >> sys.stderr, "\n\nExiting on user cancel."
    sys.exit(1)
