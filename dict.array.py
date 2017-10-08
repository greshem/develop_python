#!/us/bin/python
dict = {"timestamp": None,
        "releasestr": None,
        "arch": None,
        "discNum": None,
        "baseDir": None,
        "packagesDir": None,
        "pixmapsDir": None,
        "outfile": None}
allDiscs = None

opts_array = []
for key in dict.keys():
    opts_array.append("%s=" % (key,))
opts_array.append("allDiscs")

print dict;
print "###############################################################################"
print opts_array;

