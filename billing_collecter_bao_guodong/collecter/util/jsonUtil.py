# -*- coding:utf-8 -*-
'''
Created on 2015年9月17日

@author: baoguodong.kevin
'''
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