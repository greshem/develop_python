from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mysql_db import get_mysql_session
from get_onedomain_lastmonth_cdnflows import get_onedomain_lastmonth_cdnflows
from get_all_domainIds import get_all_domainIds
from insert_onedomain_lastmonth_cdnflows import insert_onedomain_lastmonth_cdnflows

def insert_alldomains_lastmonth_cdnflows(session):
        domainId_list=get_all_domainIds()
        domainId_list.remove('1224266')
	domainId_list.remove('1231283')
        for each in domainId_list:
	    print str(each)
            insert_onedomain_lastmonth_cdnflows(session,str(each))

if __name__=='__main__':
        session=get_mysql_session('cdn')
        insert_alldomains_lastmonth_cdnflows(session)
        session.commit()
        session.close()

