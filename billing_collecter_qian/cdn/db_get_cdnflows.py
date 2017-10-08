#!/usr/bin/env python
from   mysql_db import get_mysql_session
import datetime
from   get_all_domainIds  import get_all_domainIds


def get_local_cdnflows(domainId,dateFrom,dateTo):
	session=get_mysql_session('cdn');
	row=session.execute('select sum(flows) from cdn_flows where domain_id=\'%s\'and date>=\'%s\' and date<=\'%s\''%(domainId,dateFrom,dateTo))
	amount=0
	for each in row:
		temp=dict(zip(each.keys(),each.values()))
		amount=temp['sum(flows)']
	session.close()
	return amount


if __name__=='__main__':
    for each in  get_all_domainIds():
	    amount=get_local_cdnflows(each,'2015-09-10','2015-09-20')
	    print amount
	
	
