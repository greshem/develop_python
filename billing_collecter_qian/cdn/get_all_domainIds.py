#!/usr/bi/python
#_*_ coding: gbk -*-
import sys
import os
reload(sys)
import api.reportApi as reportApi;
import api.domainApi as domainApi, logging
import api.domainApi  as  domainApi;
import api.purgeApi   as  purgeApi;
import api.reportApi  as reportApi;
import api.requestApi as  requestApi;


def get_all_domainIds():
    logging.basicConfig(level=logging.DEBUG)
    api = domainApi.DomainApi("syscloudcdn", "491fbc7ac81e48544660")
    domains=api.listAll();
    domainId_list=[]
    for each in domains.domainSummarys:
    	#print dir( each);
        #print "cname=%s, domainId=%s, domainNam=%s "%(each.cname, each.domainId, each.domainName);
    	#'cdnServiceStatus', 'cname', 'domainId', 'domainName', 'enabled', 'serviceType', 'status']
    	#print "cname=%s, domainId=%s, domainNam=%s "%(each.cname, each.domainId, each.domainName);
    	temp=each.domainId
    	domainId_list.append(temp)
    return domainId_list


if __name__=="__main__":
	list=get_all_domainIds()
	print list

