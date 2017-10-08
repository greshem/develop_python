#!/usr/bin/python  
import sys;
sys.path.append("../")



from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
import sys;
sys.path.append("../")
from mysql_db        import get_mysql_session;

def get_vpn_pconn(session):
    if not session:
        session = get_mysql_session("neutron");


    ret=[];
    session.execute("use neutron");
    vpn_sql="SELECT id as resource_id,tenant_id,`name` as resource_name,`status` FROM neutron.vpnservices"

    for row in session.execute(vpn_sql).fetchall():
        row=dict(zip(row.keys(), row.values()));
        ret.append(row);
    return ret;


# neutron/dump_vpnservices.py  
def get_vpn():
    session = get_mysql_session("neutron");
    ret=get_vpn_pconn(session);
    session.close();
    return ret;

from get_instance  import get_instance;
if __name__=="__main__":


    vpn=get_vpn();
    for each in vpn:
        print "\t%s"%each;
