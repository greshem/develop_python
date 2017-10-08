#!/usr/bin/python
data = {"timestamp": "bbbbb1",
        "releasestr": "bbbbb2",
        "arch": "bbbbb3",
        "discNum": "bbbbb4",
        "baseDir": "bbbbb5",
        "packagesDir": "bbbbb6",
        "pixmapsDir": "bbbbb7",
        "outfile": "bbbbb9"}
for key, value in data.items():
    print  "%s -> %s "%(key, value);

