#!/usr/bin/python 
#coding:utf8
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


from json import *
#将Python dict类型转换成标准Json字符串
k=JSONEncoder().encode(array)
print(type(k))
print(k)
