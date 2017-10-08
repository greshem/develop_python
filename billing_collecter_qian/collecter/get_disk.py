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

def get_disks_pconn(session,user_id, project_id, is_system=1):
    if not session:
        session = get_mysql_session("cinder");

    ret=[];
    disk_size=0;
    #for row in session.execute('select * from  volumes  where       user_id="%s" and project_id="%s" ;'%(user_id, project_id)).fetchall():
    session.execute("use  cinder");
    for row in session.execute('select * from  volumes  where ( status != "deleted" ) and user_id="%s" and project_id="%s" ;'%(user_id, project_id)).fetchall():
    #for row in session.execute('select * from  volumes  where  bootable=0  and ( status != "deleted" )  ;').fetchall():
    #for row in session.execute('select * from  volumes  where  ( status != "deleted" )  ;').fetchall():
        row=dict(zip(row.keys(), row.values()));
        tmp={};

        id=row['id'];
        user_id=row['user_id'];
        project_id=row['project_id'];
        size=row['size'];
        disk_size+=size;
        #host=row['host'];
        bootable=row['bootable'];

        tmp['id']=id;
        tmp['user_id']=user_id;
        tmp['project_id']=project_id;
        tmp['size']=size;
        tmp['bootable']=bootable;
        ret.append(tmp);
    return (ret, disk_size);

def get_disks(user_id, project_id, is_system=1):
    disks_size=[];
    session=get_mysql_session("cinder");

    (ret, disk_size)=get_disks_pconn(session, user_id, project_id, 1); 
    session.close();
    return (ret, disk_size);

from get_instance  import get_instance;
if __name__=="__main__":
    all=get_instance();
    for each in all:
        user_id=each['user_id'];
        project_id=each['project_id'];

        (sizes,disk_size)=get_disks(user_id, project_id);
        for each in sizes:
            print each;
        print "disk_size=%d"%disk_size;
        #print "system_disk=%f"%get_system_disk_price();
        #print "cloud_disk=%f"%get_cloud_disk_price();


