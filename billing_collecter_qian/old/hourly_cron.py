#!/usr/bin/python
import time,datetime  
import os;
from  get_instance import get_instance;
t=time.time();

from send_message import   send_mq_message

#print "clock:%s"%time.clock();
#print "cur_ctime:%s\n"%time.ctime();

def mainloop():
    last=time.time();
    while 1:
        time.sleep(1);
        print "cur_time:%s\n"%time.strftime("%Y-%m-%d: %H:%M:%S", time.localtime());
        cur_time=time.time();
        print "time_diff=%d\n"%(cur_time-last);
        diff=cur_time-last;
        if (int(diff) > int(10)):
            a=get_instance();
            for each in a:
                print "MSG:%s"%each;
                send_mq_message(each);
            last=time.time();
        

	
mainloop();
