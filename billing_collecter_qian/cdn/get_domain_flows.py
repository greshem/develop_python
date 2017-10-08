#!/usr/bin/python
#_*_ coding: gbk -*-
import sys
import datetime;
import logging
import string;
import api.reportApi as reportApi
logging.basicConfig(level = logging.DEBUG)

def  get_onedomain_lastday_bandwidth(domainId):
    api = reportApi.ReportApi("syscloudcdn", "491fbc7ac81e48544660")
    TempDate=datetime.date.today()-datetime.timedelta(days=1)
    LastDate=TempDate.strftime('%Y-%m-%d')

    reportForm = reportApi.ReportForm()
    reportForm.dateFrom = "%s 00:00:00"%LastDate
    reportForm.dateTo = "%s 23:59:59"%LastDate
    reportForm.reportType = reportApi.REPORT_TYPE_5_MINUTES

    result = api.getFlowReport(reportForm, domainId)
    flows=result.getFlowPoints()
    amount=0;
    bandwidth=[];
    if flows is None:
	return 0 
    for each in  flows:
        #print each.point,each.flow;#each.getFlow();
        tmp=string.atof(each.flow.encode());
        bandwidth.append(tmp);
    return max(bandwidth);


def  get_onedomain_lastday_cdnflows(domainId):
    api = reportApi.ReportApi("syscloudcdn", "491fbc7ac81e48544660")
    TempDate=datetime.date.today()-datetime.timedelta(days=1)
    LastDate=TempDate.strftime('%Y-%m-%d')

    reportForm = reportApi.ReportForm()
    reportForm.dateFrom = "%s 00:00:00"%LastDate
    reportForm.dateTo = "%s 23:59:59"%LastDate
    reportForm.reportType = reportApi.REPORT_TYPE_DAILY

    result = api.getFlowReport(reportForm, domainId)
    flows=result.getFlowPoints()
    amount=0;
    if flows is None:
	return 0 
    for each in  flows:
        #print each.point,each.flow,each.getFlow();
        tmp=string.atof(each.flow.encode());
        amount+=tmp;
    return int(amount/1024);

def  get_onedomain_lastmonth_cdnflows(domainId): 
    api = reportApi.ReportApi("syscloudcdn", "491fbc7ac81e48544660"); 
    Lastmonth_first=str(datetime.date(datetime.date.today().year,datetime.date.today().month-1,1)); 
    Lastmonth_last=str(datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)); 
                                                                                                      
    reportForm = reportApi.ReportForm(); 
    reportForm.dateFrom = "%s 00:00:00"%Lastmonth_first                                                      
    reportForm.dateTo = "%s 23:59:59"%Lastmonth_last                                                        
    reportForm.reportType = reportApi.REPORT_TYPE_DAILY                                               
                                                                                                      
    result = api.getFlowReport(reportForm, domainId)                                                  
    flows=result.getFlowPoints()                                                                      
    amount=0;
    if flows is None:
	return 0;                                                                                         
    for each in  flows:                                                                               
        tmp=string.atof(each.flow.encode());                                                          
        amount+=tmp;                                                                                  
    return amount;                                                                                    
                                                                                                      

if __name__=="__main__":
    print "MAX_bandwidth=%s"%(get_onedomain_lastday_bandwidth("1222505"));
    import sys;
    sys.exit(0)

    from get_all_domainIds  import  get_all_domainIds;
    domains=get_all_domainIds()
    for each in domains:
        amount=get_onedomain_lastday_cdnflows(each);
        print "domain=%s amount=%f"%(each,amount);
 



