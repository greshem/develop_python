#!/usr/bin/python  
import sys;
sys.path.append("../")



from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker


from mysql_db         import  get_mysql_session;

# neutron/dump_floatingips.py  
# for row in session.execute('select * from  floatingips  where  status="ACTIVE"  ;').fetchall():
def get_ip_count(): 
    session=get_mysql_session("neutron");
    ret=get_ip_count_pconn(session);
    session.close();
    return ret;

    

def get_ip_count_pconn(session): 
    if not session:
        session = get_mysql_session("neutron");

    ips=[];

    ip_sql="SELECT floatingips.id as resource_id,floatingips.tenant_id,floating_ip_address as resource_name,floatingips.status as `status`,ports.created_at \
    FROM neutron.floatingips LEFT JOIN neutron.ports ON floatingips.floating_port_id=ports.id WHERE created_at <= DATE_FORMAT(DATE_ADD(CURRENT_TIMESTAMP,INTERVAL -1 HOUR),'%Y-%m-%d %H:%i')"

    for row in session.execute(ip_sql).fetchall():
        row=dict(zip(row.keys(), row.values()));
        ips.append(row);

    session.close();
    return  ips;

if __name__=="__main__":
    array=get_ip_count();
    for each in array:
        print "\t%s"%each;
