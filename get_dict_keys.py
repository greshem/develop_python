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

def get_dict_keys(dict):
	opts_array=[];
	for key in dict.keys():
		opts_array.append("%s=" % (key,))
	return opts_array;

print dict;
print "###############################################################################"
print get_dict_keys(dict);

