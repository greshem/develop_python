#!/usr/bin/python 
import commands

##Exec(" echo \"perl /root/bin_win7//local_ivm/lpar_info.pl \" |  socat -  TCP:10.4.17.32:8889   ",$result);
# 1|        10-597BR|         Running|       14d|      8192M|0.80|8|
# 2|         Vm-2517|         Running|       14d|     10240M|0.80|4|
# 4|         Vm-2515|         Running|       10d|     10240M|0.80|4|
# 5|         Vm-2520|         Running|       14d|      5120M|1.50|4|
# 6|         Vm-2521|         Running|       14d|      8192M|0.60|1|
#38|          lpar38|         Running|       22h|      1024M|0.80|4|0c31
#39|          lpar39|         Running|       14d|      3072M|1.10|4|
#40|          lpar40|         Running|       14d|      2048M|0.80|4|
lpar_info =commands.getoutput(" echo \"perl /root/bin_win7//local_ivm/lpar_info.pl \" |  socat -  TCP:localhost:8889     ");
print lpar_info;

ret=  [ [ each2.strip()  for each2 in each.split("|")]    for  each in  lpar_info.split("\n")];
print ret;
print "\n";

print "get lpar 1  status=%s " %(ret[0][2]);
