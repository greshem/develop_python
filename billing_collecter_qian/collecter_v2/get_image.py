#!/usr/bin/python
import sys;
sys.path.append("../")


from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

from mysql_db        import get_mysql_session;

def get_image_pconn(session): 
    if not session:
        session = get_mysql_session("nova");

    image_ref=None;

    image_sql="SELECT user_id,images.id as resource_id,project_id as tenant_id,`name` as resource_name,count(instance_image.uuid) as sum FROM (SELECT `uuid`, user_id,project_id,image_ref FROM nova.instances WHERE image_ref IS NOT NULL AND deleted=0 \
    AND vm_state != 'error' AND created_at <= DATE_FORMAT(DATE_ADD(CURRENT_TIMESTAMP,INTERVAL -1 HOUR),'%Y-%m-%d %H:%i'))\
     instance_image LEFT JOIN glance.images ON instance_image.image_ref=images.id group by images.id" 

    session.execute("use nova");
    ret=[];
    for row in session.execute(image_sql).fetchall():
        row=dict(zip(row.keys(), row.values()));
        ret.append(row);
    return ret;


def get_image(instance_id):
    session=get_mysql_session("nova");
    image_ref=None;
    image_ref=get_image_pconn(session);
    session.close();
    return image_ref;

if __name__=="__main__":

    from get_instance  import get_instance;
    from mysql_db import get_mysql_session
    db_sess= get_mysql_session("nova");
    image_ref=get_image_pconn(db_sess); 
    for each in image_ref:
        print each;


