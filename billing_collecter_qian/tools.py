import uuid
from json               import * ;
#import json               ;
from  ini_config  import  ini_get_value;
def get_uuid():
    return uuid.uuid4().__str__()

def get_my_uuid(number):
    ret_str="%032d"%number; 
    return ret_str;
    

def get_region():
    return ini_get_value("region");


def dict_to_json(dic):
    k=JSONEncoder().encode(dic)
    return k;

def json_to_dic(json_str):
    assert(isinstance(json_str,str));
    #k=JSONEncoder().decode(json_str)
    k=JSONDecoder().decode(json_str)
    #k=json.loads(json_str);
    return k;

def test_json_to_dic():

    json_str='{"route_1": 3, "disk_1_G": 100, "user_id": "user_id", "uuid": "uuid", "hour": "2015_04_06_24", "instance_1": 1, "bandwidth_1_M": 0, "image_1": 1, "memory_1024_M": 4096, "ip_1": 4, "cdnflow_1_G": 2, "vpn_1": 4, "mq_uuid": "37d33558-f6c2-425a-bc8b-102789d92771", "cpu_1_core": 16, "cdnwidthband_1_M": 2048, "project_id": "project_id", "id": "uuid", "snapshotdisk_1_G": 100}';
    print "||||%s||||"%type(json_str);
    print "||||%s||||"%json_str;
    k=json_to_dic(json_str),
    print k;
    assert( isinstance(k, tuple));

def change_keystone_userID_to_accountID(user_id):
    from mysql_db   import  get_mysql_session;
    session =  get_mysql_session("billing");
    session =  get_mysql_session("billing");
    rows=session.execute('select account_id from  account where  user_id=\"%s\"  '%user_id).fetchall();
    assert(len(rows)==1);	
    session.close();
    return rows[0]['account_id'];


if __name__=="__main__":
    print get_uuid();
    print get_region();

    test_json_to_dic();

    print get_my_uuid(1);


