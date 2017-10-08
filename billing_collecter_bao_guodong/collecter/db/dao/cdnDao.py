# -*- coding:utf-8 -*-
'''
Created on 2015年9月21日

@author: baoguodong.kevin
'''
from collecter.db.object.models import BillingResource,Using
from collecter.db.sqlalchemy import session as sa
from oslo_log import log as logging
LOG = logging.getLogger(__name__)
class CDNDao():
    def __init__(self,cdnDict=None):
        self.cdnDict=cdnDict
    
    def add_or_update(self,session=None,auto_close=True):
        if session is None:
            session=sa.get_session()
        row=session.query(Using).filter(Using.resource_id==self.using.resource_id).filter(Using.started_at==self.using.started_at).first()
        if not row:
            session.merge(self.using)
            session.flush()
        if auto_close:
            session.close()
    
    def batch_add_cdn(self,billingResources,session=None):
        
        pass