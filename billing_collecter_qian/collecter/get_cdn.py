#!/usr/bin/python  


from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from mysql_db import   get_mysql_session;
import sys;
sys.path.append("../cdn")

from   get_one_domain_flows import  get_domain_flows;
from mysql_db        import get_mysql_session;



def _get_all_tenant_id():
    session=get_mysql_session("cdn");
    ret=[];
    session.execute("use cdn");
    for row in session.execute('select * from  cdn_domain_manager_domain   ;').fetchall():
        row=dict(zip(row.keys(), row.values()));
        tenant_id=row["tenant_id"];
        ret.append(tenant_id);
    session.close();
    return ret;

    

def tenant_id_2_domain_id(tenant_id):
    session = get_mysql_session("cdn");

    ret=[];
    for row in session.execute('select * from  cdn_domain_manager_domain   where tenant_id=\"%s\";'%tenant_id).fetchall():
        row=dict(zip(row.keys(), row.values()));
        status=row["status"];
        domain_cname=row["domain_cname"];
        tenant_id=row["tenant_id"];
        domain_name=row["domain_name"];
        domain_id=row["domain_id"];
        source_type=row["source_type"];
        create_time=row["create_time"];
        Enable=row["Enable"];
        id=row["id"];
        ret.append(domain_id);

    return ret;

def get_tenant_id_flows(tenant_id):
    domain_id=tenant_id_2_domain_id(tenant_id);
    amount=0;
    for each in  domain_id:
        amount+=_get_domain_id_flow_last_month(each);
    return amount;
    
    
#FIXME: merge with  cdn/  dir  
def _get_domain_id_flow_last_month(domain_id):
        return  get_domain_flows(domain_id);

if __name__=="__main__":
    import  sys;
    for each in _get_all_tenant_id():
        print "tenant_id:%s = %fG"%(each, get_tenant_id_flows(each));
        #domain_id=tenant_id_2_domain_id_last_month(each);
        #print "python %s %s -> %s  "%( sys.argv[0],  each, domain_id);
        
    

