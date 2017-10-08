#!/usr/bin/python
#_*_ coding: gbk -*-
import sys
import datetime
#reload(sys)

import logging
import string
from api import reportApi
#import api.reportApi as reportApi
logging.basicConfig(level = logging.DEBUG)


def  get_lastday_domain_flows(domainId):
        get_domain_flows(domainId, from , to ):

def  get_lastmonth_domain_flows(domainId):
        get_domain_flows(domainId, from , to ):


    api = reportApi.ReportApi("syscloudcdn", "491fbc7ac81e48544660")
    TempDate=datetime.date.today()-datetime.timedelta(days=1)
    LastDate=TempDate.strftime('%Y-%m-%d')

    reportForm = reportApi.ReportForm()
    reportForm.dateFrom = "%s 00:00:00"%LastDate
    reportForm.dateTo = "%s 23:59:59"%LastDate
    reportForm.reportType = reportApi.REPORT_TYPE_DAILY


    print("获取一个域名的流量报表")
    result = api.getFlowReport(reportForm, domainId)
    print 'result:', result.getRet(), result.getMsg(), result.getXCncRequestId()
    flows=result.getFlowPoints()
    print 'flowPoints:%s', flows;

    #'flow', 'getFlow', 'getPoint', 'point', 'setFlow', 'setPoint']
    amount=0;
    for each in  flows:
        print each.point,each.flow,each.getFlow();
        tmp=string.atof(each.flow.encode());
        amount+=tmp;
    return amount;

if __name__=="__main__":
    pass;
    domainId = "1228328";
    amount=get_lastday_domain_flows(domainId);
    print "amount=%f"%amount;
