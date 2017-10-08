# -*- coding:utf-8 -*-
from sqlalchemy import Column, Index, Integer, BigInteger, Enum, String, schema
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, DateTime, Boolean, Text, Float,Numeric,DECIMAL
from sqlalchemy.orm import relationship, backref, object_mapper
from oslo.config import cfg

from collecter.db.sqlalchemy import models
from collecter.common import timeutils


CONF = cfg.CONF
BASE = declarative_base()

def MediumText():
    return Text().with_variant(MEDIUMTEXT(), 'mysql')


class BillingBase(
#                 models.SoftDeleteMixin,
#               models.TimestampMixin,
               models.ModelBase):
    metadata = None
    
class BillingResource(BASE,BillingBase,models.TimestampMixin):
    __tablename__ = 'billing_resource'
    __table_args__ = ()
    resource_id=Column(String(64), primary_key=True)
    resource_name=Column(String(64))
    billing_item=Column(String(64),nullable=False)
    region_id=Column(String(64),nullable=False)
    sum=Column(Integer)
    parent_id=Column(String(64))
    status=Column(String(32))
    resource_type=Column(String(32),nullable=False)
    user_id=Column(String(64))
    tenant_id=Column(String(64))
    deleted_at=Column(DateTime)

class Using(BASE,BillingBase):
    __tablename__ = 'using'
    __table_args__ = ()
    using_id=Column(String(64), primary_key=True)
    resource_id=Column(String(64), ForeignKey('billing_resource.resource_id'),nullable=False)
    created_at=Column(DateTime, default=timeutils.utcnow)
    started_at=Column(DateTime)
    ended_at=Column(DateTime)
    tran_status=Column(String(32))
    billingresource=relationship('BillingResource',enable_typechecks=False)
    
    
#
#class User(BASE,SearchBase,models.TimetampDefault):
#    """Represents a running service on a host."""
#
#    __tablename__ = 'user'
#    __table_args__ = ()
#
#    id = Column(Integer, primary_key=True,autoincrement=True)
#    username = Column(String(100),nullable=False)
#    password = Column(String(100))
#    realname = Column(String(255))
#    phone = Column(String(50))
#    telephone = Column(Integer)
#    email = Column(String(100))
#    comment = Column(String(4000))
#    type=Column(String(50))
#    state=Column(String(50))
#    isAdmin=Column(Boolean)
##    createTime = Column(DateTime, default=timeutils.utcnow,
##                              nullable=False)
##    updateTime = Column(DateTime, default=timeutils.utcnow,
##                              nullable=False)
#
#
#class Core(BASE,SearchBase,models.TimetampDefault):
#    __tablename__ = 'core'
#    __table_args__ = ()
#    id = Column(Integer, primary_key=True,autoincrement=True)
#    core=Column(String(255),nullable=False)
#    corePath=Column(String(255))
#
#
#class Corporation(BASE,SearchBase,models.TimetampDefault):
#    __tablename__ = 'corporation'
#    __table_args__ = ()
#    id = Column(Integer, primary_key=True,autoincrement=True)
#    name=Column(String(255),nullable=False)
#    info=Column(MediumText())
# 
#    
#class Role(BASE,SearchBase,models.TimetampDefault): 
#    __tablename__ = 'role'
#    __table_args__ = ()
#    id = Column(Integer, primary_key=True,autoincrement=True)
#    roleName=Column(String(100),nullable=False)
#    roleId=Column(String(100),nullable=False)
#
#
#class CoreCorporation(BASE,SearchBase,models.TimetampDefault):
#    __tablename__ = 'core_corporation'
#    __table_args__ = ()
#    id = Column(Integer, primary_key=True,autoincrement=True)
#    coreId=Column(Integer,ForeignKey('core.id'),nullable=False)
#    corporationId=Column(Integer,ForeignKey('corporation.id'),nullable=False)
#    
#class UserCorporation(BASE,SearchBase,models.TimetampDefault):
#    __tablename__ = 'user_corporation'
#    __table_args__ = ()
#    id = Column(Integer, primary_key=True,autoincrement=True)
#    userId=Column(Integer,ForeignKey('user.id'),nullable=False)
#    corporationId=Column(Integer,ForeignKey('corporation.id'),nullable=False)
#    
#class UserRole(BASE,SearchBase,models.TimetampDefault):
#    __tablename__ = 'user_role'
#    __table_args__ = ()
#    id = Column(Integer, primary_key=True,autoincrement=True)
#    userId=Column(Integer,nullable=False)
#    roleId=Column(String(100),nullable=False)
#    
#class Resource(BASE,SearchBase,models.TimetampDefault):
#    __tablename__ = 'resource'
#    __table_args__ = ()
#    id = Column(Integer, primary_key=True,autoincrement=True)
#    name=Column(String(255))
#    desc=Column(MediumText())
#    type=Column(String(50))
#    coreId=Column(Integer)
#    state=Column(String(50))
#    docId=Column(String(100))
#    scanSum=Column(Integer,default=0)
#    downloadSum=Column(Integer,default=0)
#    searchSum=Column(Integer,default=0)
#
#class LogAction(BASE,SearchBase,models.TimetampDefault):
#    __tablename__ = 'log_action'
#    __table_args__ = ()
#    id = Column(Integer, primary_key=True,autoincrement=True)
#    action=Column(String(255))
#    userId=Column(Integer)
#    username=Column(String(100))
#    hostIp=Column(String(100))
#    info=Column(MediumText())
#
#class log_data(BASE,SearchBase,models.TimetampDefault):
#    __tablename__ = 'log_data'
#    __table_args__ = ()
#    id = Column(Integer, primary_key=True,autoincrement=True)
#    docId=Column(String(100),nullable=False)
#    coreId=Column(Integer)
#    action=Column(String(100))
#    info=Column(MediumText())
#    userId=Column(Integer)
#    username=Column(String(100))
#    
#class Token(BASE,SearchBase,models.TimetampDefault):
#    __tablename__ = 'token'
#    __table_args__ = ()
#    id = Column(Integer, primary_key=True,autoincrement=True)
#    token=Column(String(50),nullable=False)
#    userId=Column(Integer)
#    username=Column(String(100))