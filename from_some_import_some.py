from curl import Curl;
import os;
import sys;
if __name__ == "__main__":
    if len(sys.argv) < 2:
        url = 'http://curl.haxx.se'
    else:
        url = sys.argv[1]
    c = Curl()
    c.get(url)
    print c.body()
    print '='*74 + '\n'
    import pprint
    pprint.pprint(c.info())
    print c.get_info(pycurl.OS_ERRNO)
    print c.info()['os-errno']
    c.close()
