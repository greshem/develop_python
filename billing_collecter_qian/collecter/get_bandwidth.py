#!/usr/bin/python  


from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

import sys;
sys.path.append("../")
from mysql_db        import get_mysql_session;

def get_bandwidth_pconn(session, instance, tenant_id):
    if not session:
        session = get_mysql_session("neutron");
    bandwidth=None;
    session.execute("use neutron");
    for row in session.execute('select * from  routers  where  tenant_id=\"%s\"  ;'%tenant_id).fetchall():
        row=dict(zip(row.keys(), row.values()));
        tenant_id=row['tenant_id'];
        id=row['id'];
        #name=row['name'];
        status=row['status'];
        admin_state_up=row['admin_state_up'];
        gw_port_id=row['gw_port_id'];
        enable_snat=row['enable_snat'];
        bandwidth=row['bandwidth'];
    return bandwidth;


def get_bandwidth(instance_id):
    session=get_mysql_session("neutron");
    bandwidth=get_bandwidth_pconn(session, instance_id);
    session.close();
    return bandwidth;


if __name__=="__main__": 

    print "bandwitdh %s"%get_bandwidth(1);
    from get_instance  import get_instance;
    from mysql_db import get_mysql_session
    session= get_mysql_session("neutron");
    all=get_instance();
    for each in all:
        uuid=each['uuid'];
        print "uuid: %s bandwidth=%s " %(uuid, get_bandwidth_pconn(session, each));

