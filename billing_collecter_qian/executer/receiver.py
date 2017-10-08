#!/usr/bin/python 
#coding=gbk
from kombu import Connection, Exchange, Queue, Consumer, eventloop
from pprint import pformat
from json               import * ;

import sys;
sys.path.append("../")

from price              import  *;
from discount           import  *;
from send_message      import  * 
from account_payment    import  reduce_money;
from mysql_db           import  get_mysql_session;
from logger             import  log_init;
from billing_item       import  billing_item_exist,billing_item_str_to_id;
from oslo_log           import  log as logging
from consumption        import  consumption_insert,consumption_record_exists;
from timeutils          import  utcnow_ts, utcnow;
from get_last_hour      import  change_hour_to_time_range;
from   datetime import *  ;
import time;



LOG = logging.getLogger(__name__)

 

#LOG = logging.getLogger(__name__)


def pretty(obj):
    return pformat(obj, indent=4)


def dict_to_str(simple_dic):
    ret_str="";
    for key, value in simple_dic.items():
        tmp="%s:%s|" % (key, value)
        ret_str+=tmp;
        ret_str+="\n";
    return ret_str;
   
def  deal_with_cdn_item(item, msg):
    LOG.info("CDN: item=%s, msg=%s"%(item,msg));

def  deal_with_one_item(item, msg):
    import re;
    assert(billing_item_exist(item)) ;
    assert(isinstance(item, str)or  isinstance(item, unicode) );
    tmp=re.split('_', item) ;
    name=tmp[0];

    user_id=msg['user_id'];
    tmp_str="get_%s_price"%name;
    price_funptr=eval(tmp_str);
    price=price_funptr();


    count=msg[item];
    billing_item_id=billing_item_str_to_id(item);
    discount=get_discount_with(user_id, billing_item_id);

    money=price*count*discount;
    LOG.info( "%s  price*discount*count=(%s * %s * %s)  = Money:%s"%(item,price, discount, count, money));
    print( "%s  price*discount*count=(%s * %s * %s)  = Money:%s"%(item,price, discount, count, money));
    money="%f"%money;
    #discount_by="cash_balance";
    from tools import  change_keystone_userID_to_accountID;
    account_id=change_keystone_userID_to_accountID(user_id);
    discount_by=reduce_money(account_id, money,item);

    tmp=re.split('_', item) ;
    resource_name=tmp[0];
    resource_type=tmp[0];

    dic={};


    account_id= change_keystone_userID_to_accountID(user_id);
    dic['account_id']=account_id;
    dic['amount']=money;
    dic['billing_item']=item;
    dic['sum'] = count;
    dic['price'] =price;
    dic['unit'] = g_dic_items[item];
    dic['discount_ratio']= discount;
    dic['resource_id']  =billing_item_str_to_id(item);
    
    dic['resource_name'] =  resource_name;
    dic['parent_id']    = "NULL";
    dic['region_id']    = "region_id";
    dic['discounted_at'] = datetime.fromtimestamp(time.time());
    dic['discount_by']   = discount_by;
    dic['resource_type'] = resource_type;
    
    if(  msg['hour'].endswith("_24")):
        LOG.info("ERROR: hour format  %s "%msg['hour']);
        return ;

    start,end= change_hour_to_time_range(str(msg['hour']));
    #start,end= change_hour_to_time_range("2015_06_01_01");
    dic['start']        = start;
    dic['end']          = end;

    if consumption_record_exists(account_id,item,start) ==0 :
        consumption_insert(dic);
    else:
        LOG.info( "SKIP, account_id=%s billing_item=%s start=%s exists "%(user_id,item,start));




#FIXME:  sql  connection session should be global var.  
def deal_with_message(msg):
    from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
    from sqlalchemy.orm import sessionmaker

    session = get_mysql_session("using");
    if(not isinstance(msg, dict)):
        LOG.info("type of msg is not  dict , instead of %s \n", type(msg));
        return;

    for each in  msg.keys():
        item=str(each);
        assert(isinstance(item, str));
        if  billing_item_exist(item):
            LOG.info("deal with %s message"%item);
            if msg['billing_item'] in ["cdnflow_1_G", "cdnbandwidth_1_M"]:
                deal_with_cdn_item(item,msg);  
            else:
                deal_with_one_item(item,msg);

        else:
            LOG.info("[%s] is metainfo , skip "%item);

    session.close();
    
    #all is done, return  ack message 
    if "using_id" in msg.keys():
        ret={};
        ret['using_id']=msg['using_id'];
        (connection, exchange)=get_mq_connection_ack();
        send_mq_message_ack_pconn(connection,exchange, ret);
        LOG.info("message_ack: %s send "%ret);
    else:
        LOG.info("ERROR: this msg have no using_id ");
    
def handle_message(body, message):
    global count;
    count=count+1;
    
    print(' Received message: %d %r' % (count,body ));
    LOG.info(' Received message: %d %r' % (count,body ));
    deal_with_message(body);
    message.ack()

    
if __name__=="__main__":
    log_init();

    global count;
    count=0
    from  send_message  import get_mq_connection;

    #with Connection('amqp://guest:guest@192.168.210.31:5672//') as connection:
    connection, exchange= get_mq_connection();
    queue = Queue('billing_collector', exchange, routing_key='billing_collector')
    with  connection:
        with Consumer(connection, queue, callbacks=[handle_message]):
            for _ in eventloop(connection):
                pass
