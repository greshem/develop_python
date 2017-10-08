
def fuck(fn):
    print "fuck %s!" % fn.__name__[::-1].upper()


def fuck2(fn):
    print "fuck %s!" % fn.__name__[::-1].upper()
    return fn()

#@fuck
#def wfg():
#    print ("in  wfg")


@fuck2
def wfg():
    print ("in  wfg")

wfg()
