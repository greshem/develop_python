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

dict2= {
		"dict2_key1":"value1",
		"dict2_key2":"value2",
		"dict2_key3":"value3",
		"dict2_key4":"value4",
		"dict2_key5":"value5",
		}


dict["arch"]=dict2;

print dict;
print "#################\n";
print dict["arch"]["dict2_key5"];
