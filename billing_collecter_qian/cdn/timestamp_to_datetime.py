#!/usr/bin/env python
import datetime
import time
def timestamp_to_lastday(timestamp):
	date=datetime.datetime.utcfromtimestamp(timestamp)
	lastday=date-datetime.timedelta(days=1)
	lastday=lastday.strftime('%Y-%m-%d')
	return lastday

def timestamp_to_lastmonth_day(timestamp):

    datedict={}
    time=datetime.datetime.utcfromtimestamp(timestamp)
    #lastmonth_firstday=str(datetime.date(time.year,time.month-1,1))
    #lastmonth_lastday=str(datetime.date(time.year,time.month,1)-datetime.timedelta(1))

    #lastmonth_firstday=str(datetime.datetime(time.year,time.month-1,1))
    #lastmonth_lastday=str(datetime.datetime(time.year,time.month,1)-datetime.timedelta(1))

    lastmonth_firstday=datetime.datetime(time.year,time.month-1,1)
    lastmonth_lastday=datetime.datetime(time.year,time.month,1)-datetime.timedelta(1)


    return  lastmonth_firstday,lastmonth_lastday

if __name__=='__main__':
    a=timestamp_to_lastday(time.time())
    print a
    start,end=timestamp_to_lastmonth_day(time.time())
    print  type(start);
    print "start=%s,end=%s"%(start,end);
