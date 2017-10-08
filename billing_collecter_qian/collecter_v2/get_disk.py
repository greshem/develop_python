#!/usr/bin/python  
import sys;
sys.path.append("../")

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

from mysql_db        import get_mysql_session;

#     54 status=available
#   1716 status=deleted
#    287 status=in-use

#  cinder/dump_volumes.py

def get_disks_pconn(session):
    if not session:
        session = get_mysql_session("cinder");

    ret=[];
    disk_size=0;
    disk_sql="SELECT id as resource_id,user_id,project_id as tenant_id,size as sum,`status`,display_name as resource_name,created_at,updated_at,deleted_at FROM cinder.volumes \
WHERE  deleted=0 AND created_at <= DATE_FORMAT(DATE_ADD(CURRENT_TIMESTAMP,INTERVAL -1 HOUR),'%Y-%m-%d %H:%i') ";

    #print disk_sql;
    session.execute("use  cinder");
    for row in session.execute(disk_sql).fetchall():
        row=dict(zip(row.keys(), row.values()));
        ret.append(row);
    return ret;

def get_disks():
    disks_size=[];
    session=get_mysql_session("cinder");

    ret=get_disks_pconn(session); 
    session.close();
    return ret;

if __name__=="__main__":
    disks=get_disks();
    for each in disks:
        print each;


