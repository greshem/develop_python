#!/user/bin/env python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mysql_db import get_mysql_session

from get_onedomain_lastday_cdnflows import get_onedomain_lastday_cdnflows
from get_all_domainIds import get_all_domainIds
from insert_onedomain_lastday_cdnflows import insert_onedomain_lastday_cdnflows

def insert_alldomains_lastday_cdnflows(session):
	domainId_list=get_all_domainIds()
	#domainId_list.remove('1224266')
	for each in domainId_list:
	    insert_onedomain_lastday_cdnflows(session,str(each))

if __name__=='__main__':
	session=get_mysql_session('cdn')
	insert_alldomains_lastday_cdnflows(session)
	session.commit()
	session.close()
