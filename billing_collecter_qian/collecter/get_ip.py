#!/usr/bin/python  
import sys;
sys.path.append("../")



from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker


from mysql_db         import  get_mysql_session;

# neutron/dump_floatingips.py  
# for row in session.execute('select * from  floatingips  where  status="ACTIVE"  ;').fetchall():
def get_ip_count(project_id): 
    session=get_mysql_session("neutron");
    ips=[];
    for row in session.execute('select * from  floatingips  where  status="ACTIVE" and tenant_id="%s"  ;'%project_id).fetchall():
        row=dict(zip(row.keys(), row.values()));

        tenant_id=row['tenant_id'];
        floating_ip_address=row['floating_ip_address'];
        router_id=row['router_id'];
        status=row['status'];

        tmp={};
        tmp['tenant_id']=tenant_id;
        tmp['floating_ip_address']=floating_ip_address;
        tmp['router_id']=router_id;
        tmp['status']=status;

        ips.append(tmp);
    session.close();
    return  ips;


def get_ip_count_pconn(session, project_id): 
    if not session:
        session = get_mysql_session("neutron");

    ips=[];
    session.execute("use neutron");
    for row in session.execute('select * from  floatingips  where  status="ACTIVE" and tenant_id="%s"  ;'%project_id).fetchall():
        row=dict(zip(row.keys(), row.values()));

        tenant_id=row['tenant_id'];
        floating_ip_address=row['floating_ip_address'];
        router_id=row['router_id'];
        status=row['status'];

        tmp={};
        tmp['tenant_id']=tenant_id;
        tmp['floating_ip_address']=floating_ip_address;
        tmp['router_id']=router_id;
        tmp['status']=status;

        ips.append(tmp);
    session.close();
    return  ips;


if __name__=="__main__":
    from get_instance  import get_instance;
    all=get_instance();
    for each in all:
        project_id=each['project_id'];
        array=get_ip_count(project_id);
        print "project_id:%s"%project_id;
        for each in array:
            print "\t%s"%each;
    #count();
    #price=get_ip_price();
    #print "ips_prices: %d  %f,  \n"%(count,price);
