#coding: utf8
import ConfigParser
from pypinyin import pinyin, lazy_pinyin


def ini_write_value():
    f = open("config.ini", "w")
    c=ConfigParser.ConfigParser()
    c.add_section("info");
    c.set("info", "key1", "网银");
    c.write(f);


def get_storage_type():
    cf = ConfigParser.RawConfigParser() 
    cf.read("config.ini") 
    storage=cf.get("info", "key1");
    return storage;

def pinyin_2_hanzi(pinyin):
    cf = ConfigParser.RawConfigParser() 
    cf.read("config.ini") 
    if cf.has_option("info", pinyin):
        storage=cf.get("info", pinyin);
        return storage;
    return pinyin;


def hanzi_2_pinying(hanzi):
    name="_".join( lazy_pinyin(unicode(hanzi,"utf8"))) 
    #print type(name);
    pinyin= name.encode("utf8");
    #print "%s -> %s"%(hanzi, pinyin);


    cf = ConfigParser.RawConfigParser() 
    cf.read("config.ini") 

    #cf.add_section("info");
    cf.set("info", hanzi, pinyin);
    cf.set("info", pinyin, hanzi);

    f = open("config.ini", "w")
    cf.write(f);
    return name.encode("utf8");

def is_chinese(uchar):
    """
    #判断一个unicode是否是汉字
    """
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False


def contains_chinese(input):
    chinese = unicode(input, "utf-8")
    for each in chinese:
        if  is_chinese(each):
            return True;
    
    return False;



if __name__=="__main__":
    import sys;
    import os;
    #ini_write_value();
    #print get_storage_type();
    #hanzi_2_pinying("网银");
    #hanzi_2_pinying("网银222");
    if len(sys.argv) != 2:
        print "Usage:   input_str ";
        sys.exit(0);

    name=sys.argv[1];
    if contains_chinese(name):
        print hanzi_2_pinying(sys.argv[1]);
    else: 
        print pinyin_2_hanzi(sys.argv[1]);

