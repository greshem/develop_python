
def repeat(object, times=None):
    global count;
    # repeat(10, 3) --> 10 10 10
    if times is None:
        while True:
            yield object
    else:
        for i in xrange(times):
            yield object+count

count=0;
for each in repeat(10,  100):
    count+=1;
    print each;
