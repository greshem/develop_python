#coding=utf8
#中文

from pymongo import MongoClient
client = MongoClient("localhost", 27017);
db = client["english"];
col=db['xdict'];

for each in col.find({"word":"image"}):
    #print "英文:%s: 中文: %s"%(each['word'],each['chinese'].encode("utf-8"));
    print "WORD: %s"%(each['word']);
    print each['chinese'];
