# -*- coding:utf-8 -*-
'''
Created on 2015年9月10日

@author: baoguodong.kevin
'''
import hashlib   

def getMD5(str):
    m2 = hashlib.md5()   
    m2.update(str)
    return m2.hexdigest()
