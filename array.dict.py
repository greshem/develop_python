#!/usr/bin/python 
#coding:gbk
#dict 对应perl 的hash 
array=[1, 2,3,4 ,5];


dict = {"timestamp": None,
        "releasestr": None,
        "arch": None,
        "discNum": None,
        "baseDir": None,
        "packagesDir": None,
        "pixmapsDir": None,
        "outfile": None}

#添加 add push_back append 
array.append(dict);
array.append(dict);
array.append(dict);
#最后一个
#print array[-1];
print array;

#size count length
print len(array);

