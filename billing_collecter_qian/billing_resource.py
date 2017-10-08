#!/usr/bin/python  


from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
import random;
from mysql_db import  get_mysql_session;
from billing_item   import  g_dic_items, billing_item_str_to_id;


def  save_to_resource_mq_buffer_pconn(session, dic):
    if session == None:     
        session=get_mysql_session("using");

    sql_str="""
INSERT delayed  INTO `using`.`billing_resource` (`resource_id`, `resource_name`, `billing_item`, `region_id`, `sum`, `parent_id`, `status`, `account_id`, `created_at`, `updated_at`, `deleted_at`, `resource_type`) VALUES ("%s", "%s", "%s", "%s", "%s","%s","%s","%s",  CURRENT_TIMESTAMP, NULL, NULL, "%s");
"""%(dic['resource_id'], dic['resource_name'],dic['billing_item'],dic['region_id'],dic['sum'], dic['parent_id'], dic['status'], dic['account_id'], dic['resource_type']);
    #print sql_str;
    session.execute(sql_str);
    #session.commit();


def  save_to_resource_mq_buffer(dic):
    assert(isinstance(dic, dict));
    session=get_mysql_session("using");
    save_to_resource_mq_buffer_pconn(session, dic);
    session.close();


def test_insert_demo():
    from random import choice

    for each in  g_dic_items.keys():
        import re;
        dic={};
        dic['resource_id']=random.randint(0,10000);
        dic['account_id']=random.randint(0,10000);
        tmp=re.split('_', each) ;
        dic['resource_name']=tmp[0];
        dic['resource_type']=tmp[0];
        dic['parent_id']="NULL";
        dic['region_id']="beijing";
        dic['sum']=choice([1,2,3,4,5,6,7,8]);
        dic['billing_item']=each;
        dic['status']=choice(["processing", "sending", "delete"]);

        save_to_resource_mq_buffer(dic);

def get_billing_resource_id_all():

    session=get_mysql_session("using");
    rows=session.execute('select distinct  resource_id from  billing_resource   ;').fetchall();
    ret= [ each['resource_id']   for each in  rows  ];
    session.close();
    return ret;

def dump1():
    session=get_mysql_session("using");
    for row in session.execute('select * from  billing_resource   ;').fetchall():
        row=dict(zip(row.keys(), row.values()));
        resource_id=row['resource_id'];
        resource_name=row['resource_name'];
        billing_item=row['billing_item'];
        region_id=row['region_id'];
        sum=row['sum'];
        parent_id=row['parent_id'];
        status=row['status'];
        account_id=row['account_id'];
        created_at=row['created_at'];
        updated_at=row['updated_at'];
        deleted_at=row['deleted_at'];
        resource_type=row['resource_type'];

        print "resource_id=%s\n"%resource_id,
#        print "resource_name=%s\n"%resource_name,
#        print "billing_item=%s\n"%billing_item,
#        print "region_id=%s\n"%region_id,
#        print "sum=%s\n"%sum,
#        print "parent_id=%s\n"%parent_id,
#        print "status=%s\n"%status,
#        print "account_id=%s\n"%account_id,
#        print "created_at=%s\n"%created_at,
#        print "updated_at=%s\n"%updated_at,
#        print "deleted_at=%s\n"%deleted_at,
#        print "resource_type=%s\n"%resource_type,

if __name__=="__main__":
    #test_insert_demo();
    dump1();
    print get_billing_resource_id_all();

