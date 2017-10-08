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
    for row in session.execute('select * from  instances   where    vm_state="active" or vm_state="stopped"  ;').fetchall():
        tmp_dic={};
        row=dict(zip(row.keys(), row.values()));

        id=row['id'];
        user_id=row['user_id'];
        project_id=row['project_id'];
        uuid=row['uuid'];

        tmp_dic['id']=id;
        tmp_dic['user_id']=user_id;
        tmp_dic['project_id']=project_id;
        tmp_dic['uuid']=uuid;
        ret.append(tmp_dic);
    return ret;

def get_instance():

    session=get_mysql_session("nova");
    ret=get_instance_pconn(session);
    session.close();
    return ret;




if __name__=="__main__":
    #instances=get_instance(); 
    session=get_mysql_session("nova");
    instances=get_instance_pconn(session);
    for each in instances:
        print each;
    session.close();
