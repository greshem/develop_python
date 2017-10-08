#!/usr/bin/python
#coding:gbk
import time,datetime                       #首先导入两个使用到的模块
string = '2009-12-09'
string = time.strptime(string,'%Y-%m-%d') #首先把字符串使用strptime()返回一个时间元素构成的元组
print string;
string[0:3]                      #把得到的时间元组前三个元素赋值给三个变量(也就是年月日)
#string = datetime.datetime(y, m, d)        #最后使用datetime把刚才得到的时间变量转为正式的时间格式变量
												#2009-12-09 00:00:00                            #至此,可以说完成了字符串到时间的转换(注意是变量类型转换的过程)  <></></> </>
