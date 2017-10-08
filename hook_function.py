def hook(each):
    print "this is hook %s"%each;

def  download(each,hook):
    hook(each);

for each in range(1,1000):
    download(each, hook);

