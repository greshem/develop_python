#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mysql_db import get_mysql_session

from get_all_domainIds import get_all_domainIds
#from get_onedomain_lastmonth_cdnflows import get_onedomain_lastmonth_cdnflows
from get_domain_flows  import get_onedomain_lastmonth_cdnflows
from get_domain_flows  import get_onedomain_lastday_cdnflows


import sys
import datetime

import logging
import string


def domain_to_userid(session,domain_id):
    row=session.execute('select tenant_id from cdn_domain_manager_domain where domain_id=\'%s\''%domain_id).fetchall()
    tenant_id=None;
    for each in row:
        temp=dict(zip(each.keys(),each.values()))
        tenant_id=temp['tenant_id']
    return  tenant_id

def insert_onedomain_lastmonth_cdnflows(session,domain_id):
    user_id=domain_to_userid(session,domain_id)
    lastmonth_flows=get_onedomain_lastmonth_cdnflows(domain_id)
    #TempDate=datetime.date.today()-datetime.timedelta(days=1)
    #LastDate=TempDate.strftime('%Y-%m-%d')
    Date=datetime.date(datetime.date.today().year,datetime.date.today().month-1,1).strftime('%Y-%m')
    session.execute('insert into cdn_flows_month(user_id,domain_id,flows,date) values(\'%s\',\'%s\',%f,\'%s\')'%(user_id,domain_id,lastmonth_flows,Date))
    session.commit()




def insert_onedomain_lastday_cdnflows(session,domain_id):
    user_id=domain_to_userid(session,domain_id)
    yesterday_flows=get_onedomain_lastday_cdnflows(domain_id)
    TempDate=datetime.date.today()-datetime.timedelta(days=1)
    LastDate=TempDate.strftime('%Y-%m-%d')
    session.execute('insert into cdn_flows(user_id,domain_id,flows,date) values(\'%s\',\'%s\',%f,\'%s\')'%(user_id,domain_id,yesterday_flows,LastDate))
    session.commit();


def insert_alldomains_lastday_cdnflows(session):
	domainId_list=get_all_domainIds()
	#domainId_list.remove('1224266')
	for each in domainId_list:
	    insert_onedomain_lastday_cdnflows(session,str(each))

def insert_alldomains_lastmonth_cdnflows(session):
        domainId_list=get_all_domainIds()
        domainId_list.remove('1224266')
	domainId_list.remove('1231283')
        for each in domainId_list:
	    print str(each)
            insert_onedomain_lastmonth_cdnflows(session,str(each))



if __name__=="__main__":

    session=get_mysql_session('cdn')
    insert_alldomains_lastmonth_cdnflows(session)
    insert_alldomains_lastday_cdnflows(session);
    session.commit()
    session.close()

