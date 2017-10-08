#!/usr/bin/python  
import sys;
sys.path.append("../")



from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

from mysql_db        import get_mysql_session;

def get_snapshotdisk_pconn(session):
    if not session:
        session = get_mysql_session("cinder");

    ret=[];
    size_amount=0;
    snapshot_sql="SELECT snapshots.id as resource_id,snapshots.created_at,snapshots.updated_at,snapshots.user_id,snapshots.project_id as tenant_id,snapshots.status,snapshots.display_name as resource_name,volumes.size as sum \
    FROM (SELECT id,created_at,updated_at,user_id,project_id,`status`,display_name,volume_id FROM cinder.snapshots WHERE deleted=0 AND created_at <= DATE_FORMAT(DATE_ADD(CURRENT_TIMESTAMP,INTERVAL -1 HOUR),'%Y-%m-%d %H:%i')) snapshots LEFT JOIN cinder.volumes ON snapshots.volume_id=volumes.id ";
    

    session.execute("use cinder");
    for row in session.execute(snapshot_sql).fetchall():
        row=dict(zip(row.keys(), row.values()));
        ret.append(row);
    return ret;

def get_snapshotdisk():
    session = get_mysql_session("cinder");
    ret= get_snapshotdisk_pconn(session);
    session.close();
    return ret;


from get_instance  import get_instance;
if __name__=="__main__":

    snapshots=get_snapshotdisk();
    for each2 in snapshots:
        print "\t%s\n"%each2;
    

    #price=get_snapshotdisk_price();
    #discount=get_discount();

    #print "size=%d*10G, price=%f, discount=%f"%(size, price, discount);
    #print "Total:%f Yuan "%(size*price*discount);
