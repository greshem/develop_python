#_*_ coding: gbk -*-
import sys
reload(sys)

if __name__ == '__main__':
    pass
import logging
import api.reportApi as reportApi

logging.basicConfig(level = logging.DEBUG)

api = reportApi.ReportApi("syscloudcdn", "491fbc7ac81e48544660")

#cname=hjdbh1802goaxl.wscloudcdn.com, domainId=1228328, domainNam=downloads.phoneunet.com 
domainId = "1228328"

reportForm = reportApi.ReportForm()
reportForm.dateFrom = "2015-09-01 01:00:00"
reportForm.dateTo = "2015-09-06 12:00:00"
#reportForm.dateFrom = "2013-10-01 01:00:00"
#reportForm.dateTo = "2013-10-18 12:00:00"

reportForm.reportType = reportApi.REPORT_TYPE_DAILY

#logging.debug("获取全部域名的流量报表")
#print ("获取全部域名的流量报表")
#result = api.getFlowReport(reportForm)
#print 'result:', result.getRet(), result.getMsg(), result.getXCncRequestId()
#print 'flowPoints:', result.getFlowPoints()
#exit(0);


logging.debug("获取某域名的流量报表")
result = api.getFlowReport(reportForm, domainId)
print 'result:', result.getRet(), result.getMsg(), result.getXCncRequestId()
print 'flowPoints:', result.getFlowPoints()
exit(0);

logging.debug("获取全部域名的请求数报表")
result = api.getHitReport(reportForm)
print 'result:', result.getRet(), result.getMsg(), result.getXCncRequestId()
print 'hitpoints:', result.getHitPoints()

logging.debug("获取某域名的请求数报表")
result = api.getHitReport(reportForm, domainId)
print 'result:', result.getRet(), result.getMsg(), result.getXCncRequestId()
print 'hitpoints:', result.getHitPoints()

logging.debug("获取某域名的log")
reportForm.reportType = None
result = api.getLog(reportForm, domainId)
print 'result:', result.getRet(), result.getMsg(), result.getXCncRequestId()
print 'logs:', result.getLogs()
