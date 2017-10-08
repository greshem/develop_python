#coding=utf-8
from IPy import IP
#ip = IP('192.168.0.0/23')
ip = IP('192.168.0.0/25')
print ip.len()    #输出192.168.0.0/16网段的IP个数
for x in ip:   #输出192.168.0.0/16网段的所有IP清单
    print(x);
