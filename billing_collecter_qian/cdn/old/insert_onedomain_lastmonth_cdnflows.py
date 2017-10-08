from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from get_onedomain_lastmonth_cdnflows import get_onedomain_lastmonth_cdnflows
from mysql_db import get_mysql_session
import datetime


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

'''
example
'''

if __name__=='__main__':
        session=get_mysql_session('cdn')
        insert_onedomain_lastmonth_cdnflows(session,'219151')
        session.close()
