# -*- coding: utf-8 -*-

from sqlalchemy import *
#from sqlalchemy.databases.mysql import *
from sqlalchemy import *
#from sqlalchemy.databases.mysql import *
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper

engine = create_engine('mysql://root:password@localhost/neutron',encoding='utf8',echo=True)


metadata = MetaData(engine)




routers_table =  Table('routers', metadata,
            Column(u'tenant_id', VARCHAR(length=255), primary_key=False),
            Column(u'id', VARCHAR(length=36), primary_key=True, nullable=False),
            Column(u'name', VARCHAR(length=255), primary_key=False),
            Column(u'status', VARCHAR(length=16), primary_key=False),
            Column(u'admin_state_up', Integer(), primary_key=False),
            Column(u'gw_port_id', VARCHAR(length=36), primary_key=False),
            Column(u'enable_snat', Integer(), primary_key=False, nullable=False, default=text(u"'1'")),
            Column(u'field_name', INTEGER(), primary_key=False),
            Column(u'bandwidth', INTEGER(), primary_key=False),
    ForeignKeyConstraint([u'gw_port_id'], [u'neutron.ports.id'], name=u'routers_ibfk_1'),
    
    )
Index(u'gw_port_id', routers_table.c.gw_port_id, unique=False)



class RoutersOrm(object):
    def __init__(self):
        pass;
    #def __repr__(self):
    #    return "%s:%s"%(self.id, self.status);    
    #__str__ = __repr__

class Routers(object):
    def __init__(self,id,name):
        self.append_id = id
        self.append_id = name
    #def __repr__(self):
    #    return "<network('%s','%s')>\n" % (self.id,self.name)
    #__str__ = __repr__



#mapper(Routers,routers_table );
mapper(RoutersOrm,routers_table );

DBSession = sessionmaker(bind=engine)
session = DBSession()
a=session.query(RoutersOrm).filter("1=1").all();
#a=session.query(Routers).filter("1=1").all();
for each in a: 
    #print each;
    #print each.bandwidth;
    print each.gw_port_id;
    print each.name;
