
def test():
    a="cccccc";
    def test2():
        print "in closure %s"%a;
        return test2;
    b=test2();
    print type(b);
    return test

c=test();
#print c;
c();
