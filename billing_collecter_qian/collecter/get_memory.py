#!/usr/bin/python 
import sys;
sys.path.append("../")

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

from mysql_db        import get_mysql_session;


def get_memory_count(uuid):
    session=get_mysql_session("nova");
    memory_mb=get_memory_count_pconn(session, uuid);
    session.close();
    return memory_mb;


def get_memory_count_pconn(session, uuid):
    if not session:
        session = get_mysql_session("nova");

    memory_mb=0;
    session.execute("use nova");
    for row in session.execute('select * from  instances  where uuid="%s"  ;'%uuid).fetchall():
        row=dict(zip(row.keys(), row.values()));
        memory_mb=row['memory_mb'];
    return  memory_mb;

    

if __name__=="__main__":
    from   get_instance   import get_instance;
    instances=get_instance(); 
    for each in instances:
        uuid=each['uuid'];
        print "uuid=%s"%uuid;
        print get_memory_count(uuid);

