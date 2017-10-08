#!/usr/bin/python  
import sys;
sys.path.append("../")

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from mysql_db  import get_mysql_session;

#vm status from    nova/api/openstack/common.py,  
#active
#building
#deleted
#error
#paused
#resized
#shelved
#shelved_offloaded
#soft_deleted
#stopped
#suspended

def get_instance_pconn(session):
    if not session:
        session = get_mysql_session("nova");

    ret=[];
    session.execute("use  nova");
    instance_sql="SELECT `uuid` as resource_id,user_id,project_id as tenant_id,display_name as resource_name,vm_state as `status`,created_at,updated_at,deleted_at,vcpus as sum,memory_mb as memory FROM nova.instances \
    WHERE deleted=0 AND vm_state != 'error' AND created_at <= DATE_FORMAT(DATE_ADD(CURRENT_TIMESTAMP,INTERVAL -1 HOUR),'%Y-%m-%d %H:%i')"

    for row in session.execute(instance_sql).fetchall():
        tmp_dic={};
        row=dict(zip(row.keys(), row.values()));
        row['billing_item']="cpu_1";
        row['region_id']="region_id";
        row['parent_id']=None;
        row['resource_type']="cpu";
        ret.append(row);


    return ret;

def get_instance():

    session=get_mysql_session("nova");
    ret=get_instance_pconn(session);
    session.close();
    return ret;




if __name__=="__main__":
    from billing_resource_assert import  keys_must_exist;
    session=get_mysql_session("nova");
    instances=get_instance_pconn(session);
    for each in instances:
        keys_must_exist(each);
        print each;
    session.close();
