# -*- coding:utf-8 -*-
def getObjFromJson(obj, jsonDict):
    if jsonDict:
        for (key, value) in jsonDict.items():
            if hasattr(obj, key):
                obj[key] = value

def getJsonFromObj(obj, notInDict=[]):
    if obj:
        jsonstr = {}
        for key in [x for x in dir(obj) if not x.startswith('_') and x not in ["get", "iteritems", "metadata", "next", "save", "update"] and x not in notInDict]:
            jsonstr[key] = getattr(obj, key)
        return jsonstr
    return None


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

import   sys;
print getJsonFromObj(BILLING_ITEM);
