
#coding: utf-8
# python中的reduce内建函数是一个二元操作函数，他用来将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给reduce中的函数 func()（必须是一个二元操作函数）先对集合中的第1，2个数据进行操作，得到的结果再与第三个数据用func()函数运算，最后得到一个结果。
#如：

#Python代码
def myadd(x,y):   
    return x+y   

sum=reduce(myadd,(1,2,3,4,5,6,7))   
print sum  

sum=reduce(lambda x,y:x+y, range(1,100));
print sum
