# -*- coding:utf-8 -*-
'''
Created on 2015年9月17日

@author: baoguodong.kevin
'''
import sys;
sys.path.append("../../../")

from collecter.db.object.models import BillingResource,Using
from collecter.db.sqlalchemy import session as sa
from oslo_log import log as logging
LOG = logging.getLogger(__name__)
from collecter.constant.billingItem import BILLING_ITEM
from collecter.util.uuidUtil import getUUID
from collecter.db.dao.billingResourceDao import BillingResourceDao
from collecter.util.jsonUtil import *
from collecter.constant.sql import SQL

from oslo.config import cfg
import datetime
import copy

CONF = cfg.CONF

class UsingDao():
    def __init__(self,using=None):
        self.using=using
    
    def add_or_update(self,session=None,auto_close=True):
#        try:
        if session is None:
            session=sa.get_session()
        session.execute('use `using` ')
        row=session.query(Using).filter(Using.resource_id==self.using.resource_id).filter(Using.started_at==self.using.started_at).first()
        if not row:
            session.merge(self.using)
            session.flush()
        if auto_close:
            session.close()
#        except Exception as e:
#            LOG.error(str(e))
    def update(self,session=None):
        if session is None:
            session=sa.get_session()
        session.merge(self.using)
        session.flush()
        session.close()
    
    def batch_add_by_billingResources(self,billingResources,resource_type,session=None):
        '''批量添加using数据库'''
        if session is None:
                session=sa.get_session()
        if billingResources:
            for billingResource in billingResources:
                if resource_type=='instance':
                    if billingResource.status=="active":
                        cpu_sum=billingResource.cpu
                        memory_sum=billingResource.memory
                        billingResourceDao=BillingResourceDao(billingResource)
                        cpu_memory_billingResources=billingResourceDao.getByParentId(session,False)
                        cpu_billingResource=None
                        memory_billingResource=None
                        for cpu_memory_billingResource in cpu_memory_billingResources:
                            if cpu_memory_billingResource.resource_type=='cpu':
                                cpu_billingResource=cpu_memory_billingResource
                            if cpu_memory_billingResource.resource_type=='memory':
                                memory_billingResource=cpu_memory_billingResource
                        if cpu_billingResource:
                            cpu_billingResource.sum=cpu_sum
                            cpu_billingResource.updated_at=billingResource.updated_at
                        else:
                            cpu_billingResource=copy.deepcopy(billingResource)
                            cpu_billingResource.resource_id=getUUID()
                            cpu_billingResource.sum=cpu_sum
                            cpu_billingResource.resource_type="cpu"
                            cpu_billingResource.region_id=CONF.region_id
#                            cpu_billingResource.region_id="RegionOne"
                            cpu_billingResource.parent_id=billingResource.resource_id
                            cpu_billingResource.billing_item=getattr(BILLING_ITEM, 'cpu')
                        if memory_billingResource:
                            memory_billingResource.sum=memory_sum
                            memory_billingResource.updated_at=billingResource.updated_at
                        else:
                            memory_billingResource=copy.deepcopy(billingResource)
                            memory_billingResource.resource_id=getUUID()
                            memory_billingResource.sum=memory_sum
                            memory_billingResource.resource_type="memory"
                            memory_billingResource.region_id=CONF.region_id
#                            memory_billingResource.region_id="RegionOne"
                            memory_billingResource.parent_id=billingResource.resource_id
                            memory_billingResource.billing_item=getattr(BILLING_ITEM, 'memory')
                        using=Using()
                        using.using_id=getUUID()
                        using.resource_id=cpu_billingResource.resource_id
                        using.billingresource=cpu_billingResource
                        d1=datetime.datetime.utcnow()
                        using.started_at=(d1-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H')
                        using.ended_at=d1.strftime('%Y-%m-%d %H')
                        self.using=using
                        self.add_or_update(session,False)
                        using.using_id=getUUID()
                        using.resource_id=memory_billingResource.resource_id
                        using.billingresource=memory_billingResource
                        self.using=using
                        self.add_or_update(session,False)
                if resource_type=='router':
                    bandwidth=billingResource.bandwidth
                    billingResourceDao=BillingResourceDao(billingResource)
                    bandwidth_billingResources=billingResourceDao.getByParentId(session,False)
                    bandwidth_billingResource=None
                    if bandwidth_billingResources:
                        bandwidth_billingResource=bandwidth_billingResources[0]
                        bandwidth_billingResource.updated_at=billingResource.updated_at
                        bandwidth_billingResource.sum=bandwidth
                    else:
                        bandwidth_billingResource=copy.deepcopy(billingResource)
                        bandwidth_billingResource.resource_id=getUUID()
                        bandwidth_billingResource.sum=bandwidth
                        bandwidth_billingResource.resource_type='bandwidth'
#                        bandwidth_billingResource.region_id="RegionOne"
                        bandwidth_billingResource.region_id=CONF.region_id
                        bandwidth_billingResource.parent_id=billingResource.resource_id
                        bandwidth_billingResource.billing_item=getattr(BILLING_ITEM, 'bandwidth')
                    using=Using()
                    using.using_id=getUUID()
                    using.resource_id=bandwidth_billingResource.resource_id
                    using.billingresource=bandwidth_billingResource
                    d1=datetime.datetime.utcnow()
                    using.started_at=(d1-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H')
                    using.ended_at=d1.strftime('%Y-%m-%d %H')
                    self.using=using
                    self.add_or_update(session,False)
                billingResource.resource_type=resource_type
                billingResource.billing_item=getattr(BILLING_ITEM, resource_type)
                billingResource.region_id=CONF.region_id
#                billingResource.region_id="RegionOne"
                billingResource.sum = billingResource.sum if billingResource.sum else 1
                using=Using()
                using.using_id=getUUID()
                using.resource_id=billingResource.resource_id
                using.billingresource=billingResource
                d1=datetime.datetime.utcnow()
                using.started_at=(d1-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H')
                using.ended_at=d1.strftime('%Y-%m-%d %H')
                self.using=using
                self.add_or_update(session,False)
        session.close()
    
    def getUsingMsg(self,session=None):
        if session is None:
            session=sa.get_session()
        session.execute('use `using` ')
        rows=session.execute(SQL.send_using).fetchall()
        result=[]
        for row in rows:
            row=dict(zip(row.keys(), row.values()))
            result.append(row)
        session.close()
        return result              


if __name__=="__main__":
    billingResource=BillingResource()
    billingResource.resource_id="123456"
    billingResource.billing_item="instance_1"
    billingResource.region_id="region1"
    billingResource.resource_type="instance"
    billingResource.sum=1

    using=Using()
    using.started_at="2015-09-17 18:00"
    using.ended_at="2015-09-17 19:00"
    using.using_id="aaaaaccbbdd11"
    using.resource_id="123456"
    using.billingresource=billingResource
    usingDao=UsingDao(using)
    usingDao.add_or_update()
