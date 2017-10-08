def logger(string):
    fh = open("/tmp/all.log", 'a')
    fh.write(string)
    fh.close();
