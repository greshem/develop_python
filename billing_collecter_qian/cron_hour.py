#!/usr/bin/python 

from    apscheduler.schedulers import *
from    apscheduler.schedulers.blocking import BlockingScheduler
from    apscheduler.executors.pool  import ThreadPoolExecutor,ProcessPoolExecutor
from    logger             import  log_init;
from    datetime      import  *; 

from    mq_buffer           import  save_to_mq_buffer;
from send_message import   send_mq_message_pconn,get_mq_connection;

from kombu import Connection, Producer, Exchange, Queue
from tree_resource import  get_resource_data
from mysql_db        import  get_mysql_session;
from billing_resource    import  save_to_resource_mq_buffer_pconn;
from using               import  save_to_using_mq_buffer_pconn;






def tick():
    print('Info: Tick! The time is: %s' % datetime.now())


def collect_res(): 
    print('Start to collect  resource at %s' % datetime.now())
    (connection,exchange)=get_mq_connection();
    session=get_mysql_session("nova");
    data=get_resource_data(session);

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

    #schedudler.add_job(collect_res, 'cron', second='0',id="one_miniuts")
    #print schedudler.get_job("one_miniuts")

    schedudler.add_job(collect_res, 'cron', hour='0-23',id="hourly")
    print schedudler.get_job("hourly")

    schedudler.start()  

"""
    #help function 
    #schedudler.add_job(tick, 'cron', second='5,10,15,20,25,30,35,40,45,50,55',id="five_second")
    #print schedudler.get_job("five_second")

    #print help(schedudler)

    #@schedudler.cron_schedule(second='*', day_of_week='0-7', hour='0-23')  
    #def quote_send_sh_job():  
    #    print 'a simple cron job start at', datetime.datetime.now()  

"""
