#!/usr/bin/python 

from mysql_db import  get_mysql_session;
from    datetime      import  *; 


#  using_id     resource_id  started ended
def get_resending_resource_ids(session):
    if session==None:
        session = get_mysql_session("using");

    ret=[];
    for row in session.execute('select * from  using.using where tran_status !="delete";').fetchall():
        row=dict(zip(row.keys(), row.values()));
        ret.append(row);
    session.close();
    return ret; 

def get_resource_from_id(session, resource_id):
    if session==None:
        session = get_mysql_session("using");

    ret={};
    rows= session.execute('select * from  using.billing_resource where resource_id=\"%s\";'%resource_id).fetchall();
    assert(len(rows) <=1 );
    ret=dict(zip(rows[0].keys(), rows[0].values()));
    session.close();
    return ret; 

    
def resend_mq():
    print('Info: Tick! The time is: %s' % datetime.now())
    from  send_message  import get_mq_connection,send_mq_message_pconn;
    session = get_mysql_session("using");
    (connection, exchange)=get_mq_connection();

    resend = get_resending_resource_ids(session);
    for each in  resend:
        resource_dict=get_resource_from_id(session, each['resource_id']);
        del  resource_dict['created_at'];
        del  resource_dict['updated_at'];
        del  resource_dict['deleted_at'];

        '''append item from   using table;'''
        resource_dict['using_id']=each['using_id'];
        resource_dict['started_at']=each['started_at'];
        resource_dict['ended_at']=each['ended_at'];
        
        #print "DDD %s"%resource_dict;
        send_mq_message_pconn(connection,exchange, resource_dict);


if __name__=="__main__":
    from    apscheduler.schedulers import *
    from    apscheduler.schedulers.blocking import BlockingScheduler
    from    apscheduler.executors.pool  import ThreadPoolExecutor,ProcessPoolExecutor

    executors = {    
                 'default': ThreadPoolExecutor(10),    
                 'processpool': ProcessPoolExecutor(3)
                 }
    job_defaults = {    
                    'coalesce': False,    
                    'max_instances':60
                    }

    schedudler = BlockingScheduler(executors=executors,job_defaults=job_defaults)
    schedudler.add_job(resend_mq, 'cron', minute='5,10,15,20,25,30,35,40,45,50,55',id="five_minute")
    print schedudler.get_job("five_minute");
    schedudler.start();


