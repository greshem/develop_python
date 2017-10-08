#coding=utf-8

from  itertools  import groupby,chain

#开发
dev= ['baoguodong', 'kongxiao', 'qianzhongjie', 'dongchangwei', 'fangzhanghe', 'huliuchen', 'yanglei', 'zhaozhongguo', 'zhangchun', 'zengweiwei' ]

#网管
netmanage= ['chenjunqing', 'xinlei', 'liuyinyan', 'pengzhu', 'luzhujun', 'sunshaoqing', 'wangzheng' ]

#dba
dba= ['dbazhanghui', 'hanchaobing'];

#sa
sa= [ 'jianghao', 'mayuchao', 'sunyu', 'shenzhongyu', 'yangjian', 'zhaozhicheng']

#--------------------------------------------------------------------------
#leader
leader=['jinxiao','shitingyu'];

#net
net= [ 'zhenxiangke', 'zhangyun', 'zhuxiang', 'wanglu', 'zhuyongqing', ]

#misc
misc=[ 'liulei', 'root', 'zhangtie', 'chengrui' ]

all_member=list(chain( dev, netmanage, dba,  sa,  leader,  net, misc));


def   catalog_user_array_3(h):
    if  h[3] in   dev:
        return "dev";
    elif  h[3] in  netmanage:
        return "netmanage";
    elif  h[3] in  dba:
        return "dba";
    elif  h[3] in  sa:
        return "sa";
    elif h[3] in leader:
        return "leader";
    elif h[3] in net:
        return "net";
    elif h[3] in misc:
        return "misc";
    else:
        return "other";

test_array=[
["aa","bb","cc","qianzhongjie"],
["aa","bb","cc","baoguodong"],
["aa","bb","cc","dongchangwei"],
["aa","bb","cc","chengrui"],
["aa","bb","cc","chenjunqing"],
["aa","bb","cc","zhangchun"],
];
output= sorted(test_array, key = catalog_user_array_3)
for each in output:
	print each;
