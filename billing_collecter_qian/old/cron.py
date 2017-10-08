#coding=utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time
import os

from tree_resource import  get_resource_data;
from send_message import   send_mq_message_pconn,get_mq_connection;
from kombu import Connection, Producer, Exchange, Queue




def tick():
    print('Tick! The time is: %s' % datetime.now())
    (connection,exchange)=get_mq_connection();
    data=get_resource_data();
    for each in data:
        print each;
        send_mq_message_pconn(connection,exchange,each);
        save_to_mq_buffer(each['mq_uuid'], each);


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick,'cron',  hour='*')    
    scheduler.add_job(tick,'cron', second="1", hour='*')   #every minutes 

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown() 


#every three second     
#scheduler.add_job(tick,'cron', second='*/3', hour='*')    

#every minuts
#scheduler.add_job(tick,'cron', second="1", hour='*')    

#
# Schedules job_function to be run on the third Friday
# of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
#    sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')

