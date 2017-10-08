from  collecter_v2.get_disk import *;
from  collecter_v2.get_image   import *
from  collecter_v2.get_ip import *
#from  collecter_v2.get_cdn import *
from  collecter_v2.get_cpu import *
from  collecter_v2.get_bandwidth import *
from  collecter_v2.get_router import *
from  collecter_v2.get_vpn import *
from  collecter_v2.get_instance import *
from  collecter_v2.get_snapshotdisk import *
from  collecter_v2.get_memory import *
from  collecter_v2.billing_resource_assert import *

from collecter_v2  import get_router ;
from mysql_db import  get_mysql_session;

#print dir(collecter_v2);
session = get_mysql_session("nova");

ret=get_router.get_user_routers_pconn(session);
ret=get_instance_pconn(session);
ret=get_disks_pconn(session);
ret=get_image_pconn(session); 
ret=get_instance_pconn(session);
ret=get_ip_count_pconn(session); 
ret=get_memory_pconn(session);
ret=get_user_routers_pconn(session);
ret=get_snapshotdisk_pconn(session);
ret=get_vpn_pconn(session);
print ret;
