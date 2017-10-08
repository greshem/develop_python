#!/usr/bin/python  
import sys;
sys.path.append("../")

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from  mysql_db   import  get_mysql_session;
from  billing_resource_assert   import  keys_must_exist;

# neutron/dump_routers.py
def  get_user_routers_pconn(session):
    if not session:
        session = get_mysql_session("neutron");

    ret=[];
    session.execute("use neutron");

    router_sql="SELECT routers.tenant_id,routers.id as resource_id,routers.name as resource_name,routers.status,ports.created_at as created_at,'10' as bandwidth  \
    FROM neutron.routers LEFT JOIN neutron.ports ON routers.gw_port_id=ports.id WHERE created_at <= DATE_FORMAT(DATE_ADD(CURRENT_TIMESTAMP,INTERVAL -1 HOUR),'%Y-%m-%d %H:%i')"
    


    for row in session.execute(router_sql).fetchall():
        row=dict(zip(row.keys(), row.values()));
        ret.append(row);
    return ret;

def  get_user_routers():
    session = get_mysql_session("neutron");
    ret=get_user_routers_pconn(session);
    session.close();
    return ret;


def _get_all_tenant_id():
    session = get_mysql_session("neutron");
    rows=session.execute('select tenant_id from  routers ;').fetchall();
    ret=[ row['tenant_id']  for row in  rows ];
    return ret;
       
if __name__=="__main__":

    routers=get_user_routers();
    for each in routers:
        print "\t%s"%each;
        #keys_must_exist(each);
