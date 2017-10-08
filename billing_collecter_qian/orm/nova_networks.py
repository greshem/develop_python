# -*- coding: utf-8 -*-
from sqlalchemy import *
#from sqlalchemy.databases.mysql import *
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper

engine = create_engine('mysql://root:password@localhost/nova',encoding='utf8',echo=True)


metadata = MetaData(engine)


networks_table =  Table('networks', metadata,
    Column(u'created_at', DATETIME(), primary_key=False),
            Column(u'updated_at', DATETIME(), primary_key=False),
            Column(u'deleted_at', DATETIME(), primary_key=False),
            Column(u'id', INTEGER(), primary_key=True, nullable=False),
            Column(u'injected', Integer(), primary_key=False),
            Column(u'cidr', VARCHAR(length=43), primary_key=False),
            Column(u'netmask', VARCHAR(length=39), primary_key=False),
            Column(u'bridge', VARCHAR(length=255), primary_key=False),
            Column(u'gateway', VARCHAR(length=39), primary_key=False),
            Column(u'broadcast', VARCHAR(length=39), primary_key=False),
            Column(u'dns1', VARCHAR(length=39), primary_key=False),
            Column(u'vlan', INTEGER(), primary_key=False),
            Column(u'vpn_public_address', VARCHAR(length=39), primary_key=False),
            Column(u'vpn_public_port', INTEGER(), primary_key=False),
            Column(u'vpn_private_address', VARCHAR(length=39), primary_key=False),
            Column(u'dhcp_start', VARCHAR(length=39), primary_key=False),
            Column(u'project_id', VARCHAR(length=255), primary_key=False),
            Column(u'host', VARCHAR(length=255), primary_key=False),
            Column(u'cidr_v6', VARCHAR(length=43), primary_key=False),
            Column(u'gateway_v6', VARCHAR(length=39), primary_key=False),
            Column(u'label', VARCHAR(length=255), primary_key=False),
            Column(u'netmask_v6', VARCHAR(length=39), primary_key=False),
            Column(u'bridge_interface', VARCHAR(length=255), primary_key=False),
            Column(u'multi_host', Integer(), primary_key=False),
            Column(u'dns2', VARCHAR(length=39), primary_key=False),
            Column(u'uuid', VARCHAR(length=36), primary_key=False),
            Column(u'priority', INTEGER(), primary_key=False),
            Column(u'rxtx_base', INTEGER(), primary_key=False),
            Column(u'deleted', INTEGER(), primary_key=False),
            Column(u'mtu', INTEGER(), primary_key=False),
            Column(u'dhcp_server', VARCHAR(length=39), primary_key=False),
            Column(u'enable_dhcp', Integer(), primary_key=False),
            Column(u'share_address', Integer(), primary_key=False),
    
    
    )

Index(u'networks_bridge_deleted_idx', networks_table.c.bridge, networks_table.c.deleted, unique=False)
Index(u'networks_vlan_deleted_idx', networks_table.c.vlan, networks_table.c.deleted, unique=False)
Index(u'networks_host_idx', networks_table.c.host, unique=False)
Index(u'networks_project_id_deleted_idx', networks_table.c.project_id, networks_table.c.deleted, unique=False)
Index(u'networks_table.c.dr_v6_idx', networks_table.c.cidr_v6, unique=False)
Index(u'uniq_networks0vlan0deleted', networks_table.c.vlan, networks_table.c.deleted, unique=True)
Index(u'networks_uuid_project_id_deleted_idx', networks_table.c.uuid, networks_table.c.project_id, networks_table.c.deleted, unique=False)

#表的创建. 
#networks.create()

class network(object):
    def __init__(self,name,description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<network('%s','%s')>" % (self.name,self.description)

    __str__ = __repr__


mapper(network,networks_table)

DBSession = sessionmaker(bind=engine)
session = DBSession()
a=session.query(network).filter("1=1").all();
print a;
#b=network("tst", "tst");
#print dir(network);
#a=networks_.select();
#b=a.execute();
#print b;

