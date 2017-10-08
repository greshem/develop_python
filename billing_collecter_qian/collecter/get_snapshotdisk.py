#!/usr/bin/python  
import sys;
sys.path.append("../")



from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

from mysql_db        import get_mysql_session;

def get_snapshotdisk_pconn(session, project_id):
    if not session:
        session = get_mysql_session("cinder");

    ret=[];
    size_amount=0;
    session.execute("use cinder");
    for row in session.execute('select * from  snapshots  where status="available" and project_id="%s" ;'%project_id).fetchall():
        row=dict(zip(row.keys(), row.values()));

        id=row['id'];
        volume_id=row['volume_id'];
        user_id=row['user_id'];
        project_id=row['project_id'];
        volume_size=row['volume_size'];
        #volume_type_id=row['volume_type_id'];
        
        tmp={};
        tmp['id']=id;
        tmp['volume_id']=volume_id;
        tmp['user_id']=user_id;
        tmp['project_id']=project_id;
        tmp['volume_size']=volume_size;
        size_amount+=volume_size;
        ret.append(tmp);
    return (ret, size_amount);



#  cinder/dump_snapshots.py 
def get_snapshotdisk(project_id):
    session = get_mysql_session("cinder");

    (ret, size_amount)= get_snapshotdisk_pconn(session,  project_id);
    session.close();
    return (ret, size_amount);


from get_instance  import get_instance;
if __name__=="__main__":

    all=get_instance();
    for each in all:
        project_id=each['project_id'];
        print "\n#==========================================================================";
        print "project_id=%s"%project_id;
        snapshots=get_snapshotdisk(project_id);
        for each2 in snapshots:
            print "\t%s"%each2;
    

    #price=get_snapshotdisk_price();
    #discount=get_discount();

    #print "size=%d*10G, price=%f, discount=%f"%(size, price, discount);
    #print "Total:%f Yuan "%(size*price*discount);
