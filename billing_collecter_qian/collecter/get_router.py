#!/usr/bin/python  
import sys;
sys.path.append("../")



from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

from  mysql_db   import  get_mysql_session;


# neutron/dump_routers.py
def  get_user_routers_pconn(session, project_id):
    if not session:
        session = get_mysql_session("neutron");

    ret=[];
    session.execute("use neutron");
    for row in session.execute('select * from  routers  where tenant_id="%s"  ;'%project_id).fetchall():
    #for row in session.execute('select * from  routers  ').fetchall():
        row=dict(zip(row.keys(), row.values()));

        tenant_id=row['tenant_id'];
        id=row['id'];
        #name=row['name'];
        status=row['status'];
        bandwidth=row['bandwidth'];

        tmp={};
        tmp['tenant_id']=tenant_id;
        tmp['id']=id;
        tmp['status']=status;
        #tmp['name']=name;
        tmp['bandwidth']=bandwidth;
        ret.append(tmp);
    return ret;


def  get_user_routers(project_id):

    
    session = get_mysql_session("neutron");
    ret=get_user_routers_pconn(session, project_id);
    session.close();
    return ret;

def _get_all_tenant_id():
    session = get_mysql_session("neutron");
    rows=session.execute('select tenant_id from  routers ;').fetchall();
    ret=[ row['tenant_id']  for row in  rows ];
    return ret;
       

if __name__=="__main__":

    for each in  _get_all_tenant_id():
        print "%s"%each;
        routers=get_user_routers(each);
        for each in routers:
            print "\t%s"%each;
