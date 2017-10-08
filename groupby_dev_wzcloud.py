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
#all_member.append("aaaaaa");
#all_member.append("bbbbbb");

#for each in all_member:
    #print each;

def   catalog(h):
    if  h in   dev:
        return "dev";
    elif  h in  netmanage:
        return "netmanage";
    elif  h in  dba:
        return "dba";
    elif  h in  sa:
        return "sa";
    elif h in leader:
        return "leader";
    elif h in net:
        return "net";
    elif h in misc:
        return "misc";
    else:
        return "other";


def change_with_group(all_member):
    array=[];
    for m, n in groupby( all_member , key = catalog):
        print "#---------------";
        print(m)
        tmp_list=list(set(n));
        print(tmp_list)
        array.extend(tmp_list);
        #print "FFFFF%s"%array;
    return array;

if __name__ == '__main__':
    tmp=change_with_group(all_member);
    assert (len(all_member) ==  len(tmp));
    assert ( sorted(all_member) ==  sorted(tmp));
    #for each in tmp:
    #    print each;
    print tmp;

