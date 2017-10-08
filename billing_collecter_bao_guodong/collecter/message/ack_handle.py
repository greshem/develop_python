# -*- coding:utf-8 -*-
'''
Created on 2015年9月22日

@author: baoguodong.kevin
'''
from collecter.db.object.models import Using
from collecter.db.dao.usingDao import UsingDao
import json
from oslo_log import log as logging
LOG = logging.getLogger(__name__)

def ack_msg(msg):
    if isinstance(msg, str):
        msg=json.loads(msg)
    using=Using()
    using.using_id=msg["using_id"]
    using.tran_status="ack"
    usingDao=UsingDao(using)
    usingDao.update()