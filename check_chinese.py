#!/usr/bin/python
#coding:utf-8
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

    



#ascii 的 遍历的方式 会出现错误, utf8 本质是ascii 
def  ascii_error_check_chinese():
    a="文字";
    #for each   utf8
    for each in a:
        if is_chinese(each): 
            print "%s is chinest "%each;
        else:
            print "is not  chinest ";


# for each  unicode  unicode 的遍历. 
def  check_ok_():
    a="文字";
    #b=a.encode();
    s2 = unicode(a, "utf-8")
    #s3=  unicode(s2, "utf-8") errrr
    for each in s2:
        if is_chinese(each): 
            print "%s is chinest "%each;
        else:
            print "is not  chinest ";
        

print  contains_chinese("我的中国")
print  contains_chinese("bbbbbba中")
print  contains_chinese("bbbbbba")

