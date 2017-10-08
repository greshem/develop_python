#!/usr/bin/python  


from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

from mysql_db import  get_mysql_session;


global g_dic_items;
g_dic_items={
'instance_1':       'yuan/hour',
'cpu_1_core':       'yuan/core.hour',
'memory_1024_M':    'yuan/1024M.hour',
'disk_1_G':         'yuan/G.hour',
'snapshotdisk_1_G': 'yuan/G.hour',
'router_1':         'yuan/hour',
'ip_1':             'yuan/hour',
'bandwidth_1_M':    'yuan/M.hour',
'cdnflow_1_G':      'yuan/G.month',
'cdnbandwidth_1_M': 'yuan/M.day',
'image_1':          'yuan/hour',
'vpn_1':            'yuan/hour',
};

def  get_billing_items():
    session =  get_mysql_session("billing");
    rows=session.execute('select billing_item from  billing_item   ;').fetchall();
    ret= [  each['billing_item'].encode()   for each in  rows ];
    session.close();
    return ret;

def  dump_billing_item():
    session =  get_mysql_session("billing");
    for row in session.execute('select * from  billing_item   ;').fetchall():
        row=dict(zip(row.keys(), row.values()));
        billing_item_id=row['billing_item_id'];
        region_id=row['region_id'];
        billing_item=row['billing_item'];
        unit=row['unit'];
        price=row['price'];
        created_at=row['created_at'];
        updated_at=row['updated_at'];
        print ("billing_item_id:%s|region_id:%s|billing_item:%s|unit:%s|price:%s|created_at:%s|updated_at:%s|\n" %(billing_item_id, region_id, billing_item, unit, price, created_at, updated_at )),
    session.close();

def list_equal_test():
    a=[1,2,3,4,5];
    b=[5,4,3,2,1];
    a.sort();
    b.sort();
    assert(a==b);


def  check_billing_item_latest():
    items_from_sql=get_billing_items();
    items=g_dic_items.keys();

    items_from_sql.sort();
    items.sort();
    if not( items_from_sql == items):
        print "PANIC: db from dic  not sync from mysql billing db, please update table:  billing_item  ";
    else:
        print "OK";
    assert( items_from_sql == items);
    
    
def billing_item_exist(item):
    return  (item in g_dic_items.keys());


def test_unit_assert():
    assert (billing_item_exist("cpu_1_core"));
    assert(billing_item_exist('bandwidth_1_M'));
    assert(billing_item_exist('cdnbandwidth_1_M'));
    assert(billing_item_exist('cdnflow_1_G'));
    assert(billing_item_exist('cpu_1_core'));
    assert(billing_item_exist('disk_1_G'));
    assert(billing_item_exist('image_1'));
    assert(billing_item_exist('instance_1'));
    assert(billing_item_exist('ip_1'));
    assert(billing_item_exist('memory_1024_M'));
    assert(billing_item_exist('router_1'));
    assert(billing_item_exist('snapshotdisk_1_G'));
    assert(billing_item_exist('vpn_1'));

def check_source_code_file():
    import   os;
    for each in   g_dic_items.keys():
        import re;
        tmp=re.split('_', each) ;
        name=tmp[0];
        if os.path.isfile('collecter/get_%s.py'%name):
            #pass
            print "OK   : get_%s.py  exists "%name;
        else:
            print "ERROR: get_%s.py not exists "%name;

def gen_function_ptr():
    import   os;
    for each in   g_dic_items.keys():
        import re;
        tmp=re.split('_', each) ;
        name=tmp[0];
        print "%s:get_%s,"%(name,name);


def billing_item_str_to_id(item_str):
    assert(billing_item_exist(item_str));
    session =  get_mysql_session("billing");
    rows=session.execute('select billing_item_id from  billing_item  where billing_item=\"%s\" ;'%item_str).fetchall();
    assert(len(rows) <=1);
    session.close();
    return str(rows[0]['billing_item_id']);



def billing_item_id_to_str(item_id):
    session =  get_mysql_session("billing");
    rows=session.execute('select billing_item from  billing_item  where billing_item_id=\"%s\" ;'%item_id).fetchall();
    assert(len(rows) <=1);
    session.close();
    return str(rows[0]['billing_item']);



def test_billing_item_str_to_id():
    for each in   g_dic_items.keys():
        print "%s= %s"%(each, billing_item_str_to_id(each));

def _get_all_ids_in_sql():
    session =  get_mysql_session("billing");
    rows=session.execute('select billing_item_id from  billing_item    ;').fetchall();
    assert(len(rows) ==12);
    ret=[ each['billing_item_id']   for each in  rows ]
    session.close();
    return ret;

def test_billing_item_id_to_str():
    
    for each in  _get_all_ids_in_sql():
        item=billing_item_id_to_str(each);
        print "id=%s str=%s "%(each, item);
        #print type(each);
        assert(item  in   g_dic_items.keys());


if __name__=="__main__":

    list_equal_test();
    check_billing_item_latest();
    test_unit_assert();

    check_source_code_file();
    gen_function_ptr();

    test_billing_item_str_to_id();
    test_billing_item_id_to_str();



