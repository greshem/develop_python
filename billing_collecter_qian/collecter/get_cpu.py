#!/usr/bin/python 

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

import sys;
sys.path.append("../")

from mysql_db        import get_mysql_session;

#persistent connection
def get_cpu_count_pconn(session,uuid):
    if not session:
        session = get_mysql_session("nova");
    vcpus=0;
    session.execute("use nova");
    for row in session.execute('select * from  instances  where uuid="%s"  ;'%uuid).fetchall():
        row=dict(zip(row.keys(), row.values()));
        vcpus=row['vcpus'];
    return vcpus;

def get_cpu_count(uuid):
    session=get_mysql_session("nova");
    vcpus=0;
    vcpus=get_cpu_count_pconn(session,uuid);
    session.close();
    return vcpus;


    

if __name__=="__main__":
    from get_instance  import get_instance;
    from mysql_db import get_mysql_session
    db_sess= get_mysql_session("nova");
    all=get_instance();
    for each in all:
        project_id=each['project_id'];
        uuid=each['uuid'];
        print "uuid%s =  %d cores"%(uuid,  get_cpu_count_pconn(db_sess, uuid));
    db_sess.close();
