# -*- coding: utf-8 -*-
# api 依赖最少的接口. 
import api.domainApi  as  domainApi;
import api.purgeApi   as  purgeApi;
import api.reportApi  as reportApi;
import api.requestApi as  requestApi;


CDN_USER="syscloudcdn";
CDN_API_KEY="491fbc7ac81e48544660";





class DomainManage(domainApi.DomainApi):
    '''封装cdn api'''
    def __init__(self, user=CDN_USER, apiKey=CDN_API_KEY):
        super(DomainManage, self).__init__(user=user, apiKey=apiKey)

    def _url_check(self, domain):
        result = domain
        if not domain.startswith('http://'):
            result = 'http://'+domain
        return result

    def verify_file_check(self, domain_url):
        '''验证文件是否存在检查'''
        try:
            memcached_servers=settings.CACHES.get("default").get("LOCATION")
            mc = memcache.Client(memcached_servers)
            domain_uuid = mc.get(domain_url)
            if domain_uuid is not None:
                url = self._url_check(domain_url)+'/'+domain_uuid+'.txt'
                html = urllib2.urlopen(url)
                if html.code == 200:
                    return True
            else:
                return False
        except Exception:
            return False




class PurgeManage(purgeApi.PurgeApi):
    '''封装初始化方法'''
    def __init__(self, user=CDN_USER, apiKey=CDN_API_KEY):
        super(PurgeManage, self).__init__(user=user, apiKey=apiKey)

class RequestManage(requestApi.RequestApi):
    '''封装初始化方法'''
    def __init__(self, user=CDN_USER, apiKey=CDN_API_KEY):
        super(RequestManage, self).__init__(user=user, apiKey=apiKey)


class ReportManage(reportApi.ReportApi):
    '''封装初始化方法'''
    def __init__(self, user=CDN_USER, apiKey=CDN_API_KEY):
        super(ReportManage, self).__init__(user=user, apiKey=apiKey)


class DomainInfo(object):
    '''domainifo 对象封装'''
    def __init__(self, pk=None, domain_name=None, source_type=None, cname=None,
                 source_address=None, status=None, create_time=None):
        """

        :rtype : object
        """
        self.id = pk
        self.domain_name = domain_name
        self.source_type = source_type
        self.domain_cname = cname
        self.source_address = source_address
        self.status = status
        self.create_time = create_time


class DataStatistics(object):
    '''DataStatistics object'''
    def __init__(self, account=None, total_flow=None, total_requests=None,
                 total_io=None, time_section=None):
        """

        :rtype : object
        """
        self.Customer_Account = account
        self.Total_Flow = total_flow
        self.Total_Requests = total_requests
        self.Total_Io = total_io
        self.Time_Section = time_section

class TenantStatistics(object):
    '''TenantStatistics object'''
    def __init__(self, domain=None, month=None, flow=None,
                 requests=None, io=None):
        """

        :rtype : object
        """
        self.domain_name = domain
        self.month = month
        self.flow = flow
        self.requests = requests
        self.io = io


class LogData(object):
    '''TenantStatistics object'''
    def __init__(self, domain=None, log_url=None, size=None,
                 begin=None, end=None):
        """

        :rtype : object
        """
        self.domain_name = domain
        self.log_url = log_url
        self.log_size = size
        self.begin = begin
        self.end = end



class MonData(object):
    '''TenantStatistics object'''
    def __init__(self, date=None, top_io=None, total_flow=None):
        """

        :rtype : object
        """
        self.date = date
        self.top_io = top_io
        self.total_flow = total_flow


class PureData(object):
    '''TenantStatistics object'''
    def __init__(self, cache_type=None, cache_time=None, status=None):
        """

        :rtype : object
        """
        self.cache_type = cache_type
        self.cache_time = cache_time
        self.status = status


def get_flow_report(dateFrom, dateTo):
    '''流量统计算法'''
    Flow = 0
    Kwag1 = {}
    report = ReportManage()
    ReportForm = reportApi.ReportForm(dateFrom=dateFrom, dateTo=dateTo, reportType='daily')
    tenant_list = [i.tenant_id for i in Domain.objects.all()]
    tenant_set = set(tenant_list)
    for i in tenant_set:
        domain_id_list = [j.domain_id for j in Domain.objects.filter(tenant_id=i) if j.domain_id is not None]
        for p in domain_id_list:
            ret = report.getFlowReport(ReportForm, p)
            flowPoints = ret.flowSummary
            if flowPoints is not None:
                Flow += float(flowPoints)
        Kwag1[i] = Flow
    return Kwag1

def get_hit_report(dateFrom, dateTo):
    '''请求数统计算法'''
    Hit = 0
    domain_hit = 0
    Kwag2 = {}
    report = ReportManage()
    ReportForm = reportApi.ReportForm(dateFrom=dateFrom, dateTo=dateTo, reportType='daily')
    tenant_list = [i.tenant_id for i in Domain.objects.all()]
    tenant_set = set(tenant_list)
    for i in tenant_set:
        domain_id_list = [j.domain_id for j in Domain.objects.filter(tenant_id=i) if j.domain_id is not None]
        for p in domain_id_list:
            ret = report.getHitReport(ReportForm, p)
            hit_list = ret.getHitPoints()
            if hit_list is not None:
                for k in hit_list:
                    domain_hit += int(k.hit)
                Hit += domain_hit
        Kwag2[i] = Hit
    return Kwag2


def get_all_data(dateFrom, dateTo):
    try:
        data = []
        hit_ret = get_hit_report(str(dateFrom), str(dateTo))
        flow_ret = get_flow_report(str(dateFrom), str(dateTo))
        for k in hit_ret:
            if (dateTo-dateFrom).days == 0:
                io = flow_ret[k]*8/24*60*60
            else:
                io = flow_ret[k]*8/(24*60*60*(dateTo-dateFrom).days)

            data.append(DataStatistics(account=k, total_flow=flow_ret[k],
                                       total_requests=hit_ret[k], total_io=io, time_section=(dateTo-dateFrom).days))
        return data
    except Exception:
        return []



def get_tenant_flow(dateFrom, dateTo, tenant_id=None):
    FLOW_DATA = 0.0
    Kwag1 = {}
    report = ReportManage()
    ReportForm = reportApi.ReportForm(dateFrom=dateFrom, dateTo=dateTo, reportType='daily')
    domain_id_list = [j.domain_id for j in Domain.objects.filter(tenant_id=tenant_id) if j.domain_id is not None]
    for i in domain_id_list:
        ret = report.getFlowReport(ReportForm, i)
        flowPoints = ret.flowSummary
        if flowPoints is not None:
            FLOW_DATA += float(flowPoints)
        Kwag1[i] = FLOW_DATA
    return Kwag1



def get_tenant_hit(dateFrom, dateTo, tenant_id=None):
    Hit = 0
    domain_hit = 0
    Kwag2 = {}
    report = ReportManage()
    ReportForm = reportApi.ReportForm(dateFrom=dateFrom, dateTo=dateTo, reportType='daily')
    domain_id_list = [j.domain_id for j in Domain.objects.filter(tenant_id=tenant_id) if j.domain_id is not None]
    for i in domain_id_list:
        ret = report.getHitReport(ReportForm, i)
        hit_list = ret.getHitPoints()
        if hit_list is not None:
            for k in hit_list:
                domain_hit += int(k.hit)
        Hit += domain_hit
        Kwag2[i] = Hit
    return Kwag2



def get_tenant_data(dateFrom, dateTo, tenant_id):
    try:
        data = []
        flow_ret = get_tenant_flow(dateFrom.strftime("%Y-%m-%d %H:%M:%S"), dateTo.strftime("%Y-%m-%d %H:%M:%S"), tenant_id)
        hit_ret = get_tenant_hit(dateFrom.strftime("%Y-%m-%d %H:%M:%S"), dateTo.strftime("%Y-%m-%d %H:%M:%S"), tenant_id)
        domain_name_list = [j for j in Domain.objects.filter(tenant_id=tenant_id) if j.domain_id is not None]
        for k in flow_ret:
            for p in domain_name_list:
                if p.domain_id == k:
                    if (dateTo-dateFrom).days == 0:
                        io = flow_ret[k]*8/24*60*60
                    else:
                        io = flow_ret[k]*8/(24*60*60*(dateTo-dateFrom).days)
                    data.append(TenantStatistics(domain=p.domain_name, month=str(dateFrom.strftime('%Y-%m')),
                                                 flow=flow_ret[k], requests=hit_ret[k], io=io))
        return data
    except Exception:
        return []



def get_purge_data(dateFrom, dateTo, tenant_id):
    try:
        data = []
        purge = PurgeManage()
        ret = purge.purgeQuery(dateFrom, dateTo)
        domain_name_list = [j.domain_name for j
                            in Domain.objects.filter(tenant_id=tenant_id) if j.domain_id is not None]
        for i in ret.getPurgeList():
            for p in i.itemList:
                for k in domain_name_list:
                    match = re.search(k, p.url)
                    if match:
                        data.append(PureData(cache_type=p.url, cache_time=i.requestDate, status=p.status))
        return data
    except Exception:
        return []


def get_mon_data(dateFrom, dateTo, tenant_id):
    data = []
    domain_data = []
    domain_id_list = [i.domain_id for i in Domain.objects.filter(tenant_id=tenant_id) if i.domain_id is not None]
    report_class = ReportManage()
    ReportForm = reportApi.ReportForm(dateFrom, dateTo, reportType='fiveminutes')
    d = {}
    IO = {}
    for i in domain_id_list:
        ret = report_class.getFlowReport(ReportForm, i)
        flowPoints = ret.getFlowPoints()
        if flowPoints is not None:
            for j in flowPoints:
                domain_data.append([j.point.strftime("%Y-%m-%d"), float('%0.2f' % (float(j.flow)))])
            for k, v in domain_data:
                d[k] = d.setdefault(k, 0.0) + float(v)
                IO[k] = IO.setdefault(k, []) + [v]
    for k in sorted(d):
        io = max(IO[k])*8/(5*60)
        data.append(MonData(date=k, top_io=io, total_flow=d[k]))
    return data



