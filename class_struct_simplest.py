# -*- coding:utf-8 -*-
'''
Created on 2015年9月17日

@author: baoguodong.kevin
'''
class BILLING_ITEM:
    instance="instance_1"
    cpu="cpu_1_core"
    memory="memory_1024_M"
    disk="disk_1_G"
    snapshot="snapshotdisk_1_G"
    router="router_1"
    ip="ip_1"
    bandwidth="bandwidth_1_M"
    cdnflow="cdnflow_1_G"
    cdnbandwidth="cdnbandwidth_1_M"
    image="image_1"
    vpn="vpn_1"
    

if __name__=="__main__":
    print  BILLING_ITEM.disk;
