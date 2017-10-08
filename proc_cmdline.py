def cmdline():
    with open("/proc/1/cmdline","rt")  as f:
        data = f.read()
    if not data:
        # may happen in case of zombie process
        print "data is empty";
        return []
    if data.endswith('\x00'):
        data = data[:-1]
    return [x for x in data.split('\x00')]

a=cmdline();
print a;
