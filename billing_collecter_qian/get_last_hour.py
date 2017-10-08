#!/usr/bin/python 
#coding=gbk
import sys;
sys.path.append("collecter/")

import	time;
import dbm;
import os;
from timeutils import utcnow,utcnow_ts;
from   datetime import *  ;
import time;

def get_cur_time():
	return time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime(time.time()))

def change_to_hour_str(time_input):
	return time.strftime("%Y-%m-%d_%H",time.localtime(time_input))
	
	
def get_last_hour():
	cur_sec=time.time()-3600;
	return time.strftime("%Y-%m-%d_%H",time.localtime(cur_sec))


def get_cur_hour():
	cur_sec=time.time()-3600;
	return time.strftime("%Y-%m-%d_%H",time.localtime(cur_sec))


class historyDb:
    def append_this_hour(self,hour):
        db = dbm.open('history.db', 'c')
        db["%s"%hour]="OK";
        db.close();

    def get_last_hour(self):
        db = dbm.open('history.db', 'c')
        last_hour=db["last_hour"];
        db.close();
        return last_hour;

    def put_last_hour(self,hour):
        db = dbm.open('history.db', 'c')
        db["last_hour"]=hour;
        db.close();

    def del_this_hour(self,hour):
        db = dbm.open('history.db', 'c')
        del db["%s"%hour];
        db.close();

    def is_in_history_hour(self, hour):
        db = dbm.open('history.db', 'c')
        if db.has_key(hour):
            print "上个小时已经计费过\n";
        else:
            print "上个小时没有计费过\n";
        db.close();


class  hour_diff: 
    def __init__(self):
        import	time;
        last_time=None;
        cur_time=time();

    def hour_is_change():
        #last_time=None;
        #cur_time=time();
        last_time_hour=change_to_hour_str(hour_diff.last_time);
        cur_time_hour=change_to_hour_str(hour_diff.cur_time);
        if	 last_time_hour ==	cur_time_hour:
        	 print "小时没有变迁";
        else:
        	 print "INFO: 小时变迁";
        

def  hour_diff_detect():
    a=historyDb();
    last_hour=get_last_hour();
    a.is_in_history_hour(last_hour);
    a.put_last_hour(last_hour)

    while [ 1 ]:
        last_hour=get_last_hour();
        if a.get_last_hour() != last_hour:
            print "[%s] 小时变迁 %s %s %s  \n"%(get_cur_time(),a.get_last_hour(),last_hour);
            a.put_last_hour(last_hour)
        else:
            print "[%s] 小时没有变化, last_hour_in_db=%s  last_hour_from_system=%s \n"%(get_cur_time(), a.get_last_hour(),last_hour);
        time.sleep(10);

# time.strftime("%Y-%m-%d_%H",time.localtime(time))
def  change_hour_to_time_range(str_hour):
    assert(isinstance(str_hour, str));
    import re;
    re1=re.compile('.*-.*-.*_.*');
    re2=re.compile('.*_.*_.*_.*');

    start=None;
    if(re1.match(str_hour)):
        start = time.mktime(time.strptime(str_hour,'%Y-%m-%d_%H')); 
    elif re2.match(str_hour):
        start = time.mktime(time.strptime(str_hour,'%Y_%m_%d_%H')); 

    end=start+3600-1;

    return  datetime.fromtimestamp(start),  datetime.fromtimestamp(end); 

    
def time_to_datetime(int_time):
    assert(isinstance(int_time, int));
    tm=time.localtime(int_time);


    
    
def test_time_to_datetime():
    tm=time.localtime(time.time());
    tm1=time.localtime(time.time()-3599);
    print type(datetime.now());
    print datetime(1,2,3,0,0,0);
    print datetime(tm[0],tm[1],tm[2],tm[3],tm[4],tm[5]).strftime("TEST_%Y_%m_%d-%H");
    print datetime(tm[0],tm[1],tm[2],tm[3],tm[4],tm[5]).strftime("TEST_%Y_%m_%d-%H");
    print datetime(tm1[0],tm1[1],tm1[2],tm1[3],tm1[4],tm1[5]).strftime("TEST_%Y_%m_%d-%H");
    print datetime.now().strftime("%Y%m%d")  ;


    print utcnow();
    print type(utcnow());
    print utcnow_ts();
    print type(utcnow_ts());
    print type(date.fromtimestamp(time.time())); 
    print type(date.fromtimestamp(time.time()-3600)); 
    print type(datetime.fromtimestamp(time.time()-3600)); 


if __name__=="__main__":
    #hour_diff_detect();

    print  type(time.time());

    print time.localtime(3.333);

    #print ("%s")%get_last_hour();

    a,b= change_hour_to_time_range("2015-01-01_4");
    print "FFFF%s"%(a);
    print a.strftime("%Y_%m_%d-%T");
    print b.strftime("%Y_%m_%d-%T");
    #print type(b);



    test_time_to_datetime();


    #Out[28]: '20130810'  


    #print get_last_hour();
    #before_one_hour=get_last_hour();
    #last_time_hour= get_cur_hour();
    #cur_hour=get_cur_hour();
    #if( last_hour != cur_hout)
    #del_this_hour(last_hour);
    #is_in_history_hour(last_hour);

    #while 1:
    #    a=hour_diff();
    #    b=hour_diff();
    #    a.hour_is_change();
    #print "#添加  last_hour %s "%last_hour;
    #append_this_hour(last_hour);
    #is_in_history_hour(last_hour);

