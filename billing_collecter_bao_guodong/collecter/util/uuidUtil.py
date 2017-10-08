# -*- coding:utf-8 -*-
'''
Created on 2014-7-17

@author: baoguodong.kevin
'''
import uuid

""" 随机生成字符串 """
def getUUID():
    return uuid.uuid4().__str__()

