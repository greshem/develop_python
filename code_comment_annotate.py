#coding:gbk 
#!/usr/bin/python

#一定要在第二行， 或者第一行写上 上面的东西, 然后才可以写中文注释. 
f = open("output.txt", "w")
########################################################################
#这是中文注释
f.write("%f\n" % 1111111111)
f.write("%s\n" % 2222222222)
f.write("%s\n" % 333333333)

