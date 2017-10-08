#!/usr/bin/python
data = {"timestamp": "bbbbb",
        "releasestr": "bbbbb",
        "arch": "bbbbb",
        "discNum": "bbbbb",
        "baseDir": "bbbbb",
        "packagesDir": "bbbbb",
        "pixmapsDir": "bbbbb",
        "outfile": "bbbbb"}

data2 = {"timestamp": "ccccc",
        "releasestr": "ccccc",
        "arch": "ccccc",
        "discNum": "ccccc",
        "baseDir": "ccccc",
        "packagesDir": "ccccc",
        "pixmapsDir": "ccccc",
        "outfile": "ccccc"}

data.update(data2);
print data;
