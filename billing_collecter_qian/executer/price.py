#!/usr/bin/python
#coding=gbk

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from  mysql_db import   get_mysql_session;
from  billing_item   import  billing_item_exist,g_dic_items;


#
def get_price_pconn(session, item):
    assert(billing_item_exist(item));
    rows= session.execute('select * from billing_item where billing_item="%s" ;'%item).fetchall();
    price=0;
    assert len(rows)<=1;
    for row in  rows:
        row=dict(zip(row.keys(), row.values()));
        billing_item_id=row['billing_item_id'];
        region_id=row['region_id'];
        billing_item=row['billing_item'];
        unit=row['unit'];
        price=row['price'];
        created_at=row['created_at'];
        updated_at=row['updated_at'];
    return price;
    


def get_instance_price():
    session = get_mysql_session("billing");
    price=get_price_pconn(session, "instance_1");
    session.close();
    return price;


def get_cpu_price():
    session = get_mysql_session("billing");
    price=get_price_pconn(session, "cpu_1_core");
    session.close();
    return price;


def get_ip_price():
    session = get_mysql_session("billing");
    price=get_price_pconn(session, "ip_1");
    session.close();
    return price;

def get_bandwidth_price():
    session = get_mysql_session("billing");
    price=get_price_pconn(session, "bandwidth_1_M");
    session.close();
    return price;

def get_snapshotdisk_price():
    session = get_mysql_session("billing");
    price=get_price_pconn(session, "snapshotdisk_1_G");
    session.close();
    return price;

def  get_disk_price():
    session = get_mysql_session("billing");
    price=get_price_pconn(session, "disk_1_G");
    session.close();
    return price;


def  get_memory_price():
    session = get_mysql_session("billing");
    price=get_price_pconn(session, "memory_1024_M");
    session.close();
    return price;


def  get_router_price():
    session = get_mysql_session("billing");
    price=get_price_pconn(session, "router_1");
    session.close();
    return price;



def  get_cdnflow_price():
    session = get_mysql_session("billing");
    price=get_price_pconn(session, "cdnflow_1_G");
    session.close();
    return price;


def  get_cdnbandwidth_price():
    session = get_mysql_session("billing");
    price=get_price_pconn(session, "cdnbandwidth_1_M");
    session.close();
    return price;


#现在对image 简单处理, 镜像不收费, price 为0
def  get_image_price():
    session = get_mysql_session("billing");
    price=get_price_pconn(session, "image_1");
    session.close();
    assert(price==0);
    return price;


def  get_vpn_price():
    session = get_mysql_session("billing");
    price=get_price_pconn(session, "vpn_1");
    session.close();
    return price;


#必然报错, 不支持 example_1 item 
def  get_example_price():
    session = get_mysql_session("billing");
    price=get_price_pconn(session, "example_1");
    session.close();
    return price;


def billing_item_function_ptr_testing():
    import   os;
    print "#print price  with dynamic  generated function ";
    for each in   g_dic_items.keys():
        import re;
        tmp=re.split('_', each) ;
        name=tmp[0];
        fun_name="get_%s_price"%name;
        fun_ptr=eval(fun_name);
        print "%s=%s"%(fun_name, fun_ptr());


def manual_function_test():
    print "\n#print price  with manual generated function ";
    print "instance=%s"%get_instance_price();
    print "cpu_core=%s"%get_cpu_price();
    print "ip=%s"%get_ip_price();
    print "bandwidth=%s"%get_bandwidth_price();
    print "snapshot=%s"%get_snapshotdisk_price();
    print "cloud_disk=%s"%get_disk_price();
    print "memeory=%s"%get_memory_price();
    print "router=%s"%get_router_price();
    print "cdnflow=%s"%get_cdnflow_price();
    print "cdnbandwitdh=%s"%get_cdnbandwidth_price();
    print "image=%s"%get_image_price();
    print "vpn=%s"%get_vpn_price();

if __name__=="__main__":
    billing_item_function_ptr_testing();
    manual_function_test();

