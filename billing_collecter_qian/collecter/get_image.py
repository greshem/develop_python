#!/usr/bin/python
import sys;
sys.path.append("../")


from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

from  discount  import get_discount;
from  price     import get_cpu_price;
from mysql_db        import get_mysql_session;

def get_image_pconn(session, instance_id): 
    if not session:
        session = get_mysql_session("nova");

    image_ref=None;
    session.execute("use nova");
    for row in session.execute('select * from  instances  where uuid="%s"  ;'%uuid).fetchall():
        row=dict(zip(row.keys(), row.values()));
        image_ref=row['image_ref'];
    return image_ref;


def get_image(instance_id):
    session=get_mysql_session("nova");
    image_ref=None;
    image_ref=get_cpu_count_pconn(session,uuid);
    session.close();
    return image_ref;

if __name__=="__main__":
    from get_instance  import get_instance;
    from mysql_db import get_mysql_session
    db_sess= get_mysql_session("nova");
    all=get_instance();
    for each in all:
        uuid=each['uuid'];
        image_ref=get_image_pconn(db_sess, uuid); 
        if image_ref:
            print  "image_ref=%s"%image_ref;


