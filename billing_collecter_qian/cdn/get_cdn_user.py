#!/usr/bin/python 
from  mysql_db  import get_mysql_session;


def get_all_domains_in_cdn():

    session=get_mysql_session("cdn");
    ret=[];
    
    for row in session.execute('select * from  cdn_domain_manager_domain   ;').fetchall():
        row=dict(zip(row.keys(), row.values()));
        id=row['id'];
        tenant_id=row['tenant_id'];
        domain_id=row['domain_id'];
        domain_name=row['domain_name'];
        domain_cname=row['domain_cname'];
        create_time=row['create_time'];
        source_type=row['source_type'];
        status=row['status'];
        Enable=row['Enable'];
        tmp={};
        #domain_to_user[domain_id]=tenant_id;
        #print "tenant_id=%s"%tenant_id;
        tmp['tenant_id']=tenant_id;
        tmp['domain_id']=domain_id;
        ret.append(tmp);
    session.close();
    return ret;


print get_all_domains_in_cdn();

