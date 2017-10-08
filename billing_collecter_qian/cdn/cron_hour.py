#!/usr/bin/python 

import sys;
sys.path.append("../")

from    apscheduler.schedulers import *
from    apscheduler.schedulers.blocking import BlockingScheduler
from    apscheduler.executors.pool  import ThreadPoolExecutor,ProcessPoolExecutor
from    logger             import  log_init;
from    datetime      import  *; 

from    mq_buffer           import  save_to_mq_buffer;
from send_message import   send_mq_message_pconn,get_mq_connection;

from kombu import Connection, Producer, Exchange, Queue

from mysql_db        import  get_mysql_session;
from billing_resource    import  save_to_resource_mq_buffer_pconn;
from using               import  save_to_using_mq_buffer_pconn;
from  cdn_resource import   get_cdn_resource_data;







def tick():
    print('Info: Tick! The time is: %s' % datetime.now())


def collect_cdn_res(): 
    print('Start to collect  resource at %s' % datetime.now())
    (connection,exchange)=get_mq_connection();
    session=get_mysql_session("nova");
    data=get_cdn_resource_data();

    global count;
    count=0
    for each in data:
        print each;
        count=count+1;
        send_mq_message_pconn(connection,exchange,each);
        save_to_resource_mq_buffer_pconn(session,each);
        save_to_using_mq_buffer_pconn(session, each['mq_uuid'], each['resource_id']);
        if count==1024:
            session.commit();
            count=0;

    session.close();
    print('end of  collecting   resource at %s' % datetime.now())
    

if __name__=="__main__":
    executors = {    
                 'default': ThreadPoolExecutor(10),    
                 'processpool': ProcessPoolExecutor(3)
                 }
    job_defaults = {    
                    'coalesce': False,    
                    'max_instances':60
                    }

    log_init();
    schedudler = BlockingScheduler(executors=executors,job_defaults=job_defaults)

    schedudler.add_job(collect_cdn_res, 'cron', second='0',id="one_miniuts")
    print schedudler.get_job("one_miniuts")

    schedudler.add_job(collect_cdn_res, 'cron', day='0-7',id="dailiy")
    print schedudler.get_job("dailiy")

    schedudler.start()  
