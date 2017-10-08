#!/usr/bin/python  

from sqlalchemy     import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from mysql_db       import get_mysql_session
from billing_item   import  g_dic_items, billing_item_str_to_id;
from account_payment  import  get_account_ids;
from timeutils      import  utcnow_ts, utcnow;
from get_last_hour  import get_last_hour, change_hour_to_time_range;

from logger             import  log_init;

from oslo_log           import  log as logging

LOG = logging.getLogger(__name__)


def insert_sql_example():
    from random import choice
    ret=[];
    for each in  g_dic_items.keys():
        import re;
        tmp=re.split('_', each) ;
        resource_name=tmp[0];
        resource_type=tmp[0];
        parent_id="NULL";
        region_id="beijing";

        users=get_account_ids();
        #account_id=choice(users);
        account_id=users[0];
        
        billing_item=each;
        unit=g_dic_items[each];
        resource_id=billing_item_str_to_id(each);
        
        discount_by=choice( ["cash_balance",  "gift_balance"]);
        discount_ratio=choice([0.8,0.7,0.9,0.9,0,1]);
        sum=choice([1,2,3,4,5,6,7,8]);
        price=choice([0.1,0.2,0.3,0.4,0.5]);
        amount=discount_ratio*price*sum;

        #start=utcnow_ts();
        #end=utcnow_ts();
        discounted_at=utcnow();
        last_hour=get_last_hour();
        start,end=change_hour_to_time_range(last_hour);


        dic={};

        dic['account_id']=account_id;
        dic['amount']=amount;
        dic['billing_item']=billing_item;
        dic['sum'] = sum;
        dic['price'] =price;
        dic['unit'] =unit;
        dic['discount_ratio']= discount_ratio;
        dic['resource_id']  =resource_id;
        dic['resource_name'] =  resource_name;
        dic['parent_id']    = "NULL";
        dic['region_id']    = region_id;
        dic['discounted_at'] = discounted_at;
        dic['discount_by']   = discount_by;
        dic['resource_type'] = resource_type;
        dic['start']        = start;
        dic['end']          = end;

        if consumption_record_exists(account_id,billing_item,start) ==0 :
            consumption_insert(dic);
        else:
            LOG.info( "SKIP, account_id=%s billing_item=%s start=%s exists "%(account_id,billing_item,start));
            

        #consumption_id, account_id, amount, billing_item, sum, price, unit, discount_ratio, resource_id, resource_name, parent_id, region_id, discounted_at, discount_by, resource_type, start,end )
        

def consumption_insert(dic):
        sql_str="""
INSERT INTO `billing`.`consumption` VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, '%s', '%s', '%s', '%s','%s', '%s');""" %(dic['account_id'], dic['amount'], dic['billing_item'], dic['sum'], dic['price'], dic['unit'], dic['discount_ratio'], dic['resource_id'], dic['resource_name'], dic['parent_id'], dic['region_id'], dic['discounted_at'], dic['discount_by'], dic['resource_type'], dic['start'], dic['end']);
        print sql_str;

        session = get_mysql_session("billing");
        session.execute('%s'%sql_str);
        session.commit();
        session.close();

def consumption_record_exists(user,item,start):
    session = get_mysql_session("billing");
    #print('select * from  consumption  where  start="%s"'%time);
    rows=session.execute('select * from  consumption  where  account_id="%s" and billing_item="%s" and start="%s"  '%(user, item, start  )).fetchall();
    #print rows;
    count=len(rows);
    assert(count<=1);
    session.close();
    return count;


def dump_consumption():
    session = get_mysql_session("billing");
    for row in session.execute('select * from  consumption   ;').fetchall():
        row=dict(zip(row.keys(), row.values()));
        consumption_id=row['consumption_id'];
        account_id=row['account_id'];
        amount=row['amount'];
        billing_item=row['billing_item'];
        sum=row['sum'];
        price=row['price'];
        unit=row['unit'];
        discount_ratio=row['discount_ratio'];
        resource_id=row['resource_id'];
        resource_name=row['resource_name'];
        parent_id=row['parent_id'];
        region_id=row['region_id'];
        discounted_at=row['discounted_at'];
        discount_by=row['discount_by'];
        resource_type=row['resource_type'];
        start=row['start'];


        print "consumption_id=%s\n"%consumption_id,
        print "account_id=%s\n"%account_id,
        print "amount=%s\n"%amount,
        print "billing_item=%s\n"%billing_item,
        print "sum=%s\n"%sum,
        print "price=%s\n"%price,
        print "unit=%s\n"%unit,
        print "discount_ratio=%s\n"%discount_ratio,
        print "resource_id=%s\n"%resource_id,
        print "resource_name=%s\n"%resource_name,
        print "parent_id=%s\n"%parent_id,
        print "region_id=%s\n"%region_id,
        print "discounted_at=%s\n"%discounted_at,
        print "discount_by=%s\n"%discount_by,
        print "resource_type=%s\n"%resource_type,
        print "start=%s\n"%start;


        print ("consumption_id:%s|account_id:%s|amount:%s|billing_item:%s|sum:%s|price:%s|unit:%s|discount_ratio:%s|resource_id:%s|resource_name:%s|parent_id:%s|region_id:%s|discounted_at:%s|discount_by:%s|resource_type:%s|\n" %(consumption_id, account_id, amount, billing_item, sum, price, unit, discount_ratio, resource_id, resource_name, parent_id, region_id, discounted_at, discount_by, resource_type ));

if __name__=="__main__":
    log_init();
    insert_sql_example();
    #dump_consumption();

    #start,end= change_hour_to_time_range("2015-09-10_21");
    #consumption_record_exists("0e8cdaa354ec4e96b0258c5b4b18ecad", "cdnflow_1_G",start);

