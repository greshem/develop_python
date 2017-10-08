import sys
import os
reload(sys)

if __name__ == '__main__':
    pass
import api.domainApi as domainApi, logging

logging.basicConfig(level=logging.DEBUG)

api = domainApi.DomainApi("syscloudcdn", "491fbc7ac81e48544660")

domains=api.listAll();
#print dir(b);
for each in domains.domainSummarys:
    #print dir( each);
    #'cdnServiceStatus', 'cname', 'domainId', 'domainName', 'enabled', 'serviceType', 'status']
    print "cname=%s, domainId=%s, domainNam=%s "%(each.cname, each.domainId, each.domainName);

