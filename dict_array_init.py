#!/us/bin/python
data = {"timestamp": None,
        "releasestr": None,
        "arch": None,
        "discNum": None,
        "baseDir": None,
        "packagesDir": None,
        "pixmapsDir": None,
        "outfile": None}
allDiscs = None

opts = []
for key in data.keys():
    opts.append("%s=" % (key,))
opts.append("allDiscs")

print data;
print "###############################################################################"
print opts;

