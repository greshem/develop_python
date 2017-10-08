# -*- coding:utf-8 -*-
'''
Created on 2015年9月17日

@author: baoguodong.kevin
'''
from collecter.db.object.models import BillingResource,Using
from collecter.db.dao.usingDao import UsingDao
from collecter.db.sqlalchemy import session as sa
from oslo_log import log as logging
LOG = logging.getLogger(__name__)
from collecter.util.jsonUtil import *
from collecter.constant.sql import SQL

class InstanceBillingResource(BillingResource):
    cpu=0
    memory=0
    
class RouterBillingResource(BillingResource):
    bandwidth=0

def getResources(resource_type,session=None):
    '''得到资源的数据'''
    if session is None:
        session=sa.get_session()
    if not hasattr(SQL, resource_type):
        raise
    rows=session.execute(getattr(SQL, resource_type)).fetchall()
    result=[]
    for row in rows:
        row=dict(zip(row.keys(), row.values()))
        result.append(getBillingResourceByDict(getBillingResourceByType(resource_type),row))
    session.close()
    return result

def getBillingResourceByDict(obj,row):
    getObjFromJson(obj, row)
    return obj

def getBillingResourceByType(resource_type):
    result ={
     'instance':InstanceBillingResource,
     'router':RouterBillingResource
     }
    return result.get(resource_type,BillingResource)()

    

if __name__=="__main__":
    for obj in getResources("volumn"):
        print obj.resource_name
#    print type(getBillingResourceByType("router"))
    