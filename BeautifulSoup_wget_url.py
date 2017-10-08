
from BeautifulSoup import BeautifulSoup
import urllib2
import re

def grabHref(url,localfile):
    html = urllib2.urlopen(url).read()
    html = unicode(html,'gb2312','ignore').encode('utf-8','ignore')
    content = BeautifulSoup(html).findAll('a')

    myfile = open(localfile,'w')

    pat = re.compile(r'href="([^"]*)"')
    pat2 = re.compile(r'http')
    catalog= re.compile(r'(/open-source/.*)');

    for item in content:
        h = pat.search(str(item))
        href = h.group(1) ;
        
        h2=catalog.search(href);
        if h2:
            print h2.group(1);
            
def main():
    for each in range(1,11):
        url = "http://mvnrepository.com/open-source?p=%s"%(each);
        print  url;
        grabHref(url,"localfile")

if __name__=="__main__":
    main()
