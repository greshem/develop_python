
from horizon.utils.memoized import memoized  # noqa
import time;

@memoized
def long_time():
    print "sleep 10";
    time.sleep(10);
    return 33333;

while  1:
    print long_time();
    
