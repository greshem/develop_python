#!/usr/bin/python  
import sys;
sys.path.append("../")



from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
import sys;
sys.path.append("../")
from mysql_db        import get_mysql_session;

def get_vpn_pconn(session,project_id):
    if not session:
        session = get_mysql_session("neutron");


    ret=[];
    session.execute("use neutron");
    #for row in session.execute('select * from  vpnservices   ;').fetchall():
    for row in session.execute('select * from  vpnservices  where  tenant_id="%s" ;'%project_id).fetchall():
        row=dict(zip(row.keys(), row.values()));

        tenant_id=row['tenant_id'];
        id=row['id'];
        status=row['status'];
        subnet_id=row['subnet_id'];
        router_id=row['router_id'];

        tmp={};
        tmp['id']=id;
        tmp['tenant_id']=tenant_id;
        tmp['status']=status;
        tmp['subnet_id']=subnet_id;
        tmp['router_id']=router_id;
        ret.append(tmp);
    return ret;


# neutron/dump_vpnservices.py  
def get_vpn(project_id):
    session = get_mysql_session("neutron");
    ret=get_vpn_pconn(session, project_id);
    session.close();
    return ret;

from get_instance  import get_instance;
if __name__=="__main__":

    all=get_instance();
    for each in all:
        project_id=each['project_id'];
        print "\n#==========================================================================";
        print "project_id=%s"%project_id;
        vpn=get_vpn(project_id);
        if(len(vpn)==0):
            #print "\thave no vpn settings;",
            tmp=None;
		elif ( len(vpn)==1):
			print "len is 1\n";
        else:
            for each2 in vpn:
                print "\t%s"%each2;
