# -*- coding:utf-8 -*-
'''
Created on 2015年9月22日

@author: baoguodong.kevin
'''
from collecter.db.dao.usingDao import UsingDao
import json
from oslo_log import log as logging
from collecter.rabbitmq.producer import *
LOG = logging.getLogger(__name__)

def send_data_msg():
    usingDao=UsingDao()
    datas=usingDao.getUsingMsg()
    for data in datas:
        send_msg(data)