# -*- coding:utf-8 -*-
'''
Created on 2015年9月17日

@author: baoguodong.kevin
'''
from collecter.db.object.models import BillingResource
from collecter.db.sqlalchemy import session as sa
from oslo_log import log as logging
LOG = logging.getLogger(__name__)

class BillingResourceDao():
    def __init__(self,billingResource=None):
        self.billingResource=billingResource
    
    def getByParentId(self,session=None,auto_close=True):
        if session is None:
            session=sa.get_session()
        session.execute('use `using` ')
        billingResources=session.query(BillingResource).filter(BillingResource.parent_id==self.billingResource.resource_id).all()
        if auto_close:
            session.close()
        return billingResources
    
        