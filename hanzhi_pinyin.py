
#coding: utf-8
import string ;
import  commads;

from pypinyin import pinyin, lazy_pinyin

def test: 
    a="网银abc" 
    name="_".join( lazy_pinyin(unicode(a,"utf8"))) 
    #print type(name);
    print "%s -> %s"%(a, name.encode("utf8"));



#for each in b:
#    print each;
