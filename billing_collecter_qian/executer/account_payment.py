#!/usr/bin/python  
import sys;
sys.path.append("collecter/")



from sqlalchemy     import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

from mysql_db       import get_mysql_session;
from billing_item   import billing_item_exist;
from oslo_log       import log as logging
#from consumption    import consumption_insert;

LOG = logging.getLogger(__name__)





def get_account_ids():
    session = get_mysql_session("billing");
    ret=[];
    for row in session.execute('select account_id from  account   ;').fetchall():
        row=dict(zip(row.keys(), row.values()));
        account_id=row['account_id'];
        ret.append(account_id);
    return ret; 



def reduce_money(account_id,money,item):
    assert( billing_item_exist(item));
    assert(isinstance(money, str) or isinstance(money, unicode)  ) ;
    assert(isinstance(account_id, str) or isinstance(account_id, unicode) );

    session = get_mysql_session("billing");
    LOG.info( 'select account_id from  account  where account_id=\"%s\"   ;'%account_id);
    #rows=session.execute('select account_id from  account  where account_id=\"%s\"   ;'%account_id).fetchall();
    rows=session.execute('select user_id from  account  where user_id=\"%s\"   ;'%account_id).fetchall();
    assert( len(rows) ==1);
    reduce_from="gift_balance";

    if( get_gift_balance(account_id) > 0):
        LOG.info("#reduce_money in  gift_balance ");
        session.execute("update  account  set  gift_balance=gift_balance-%s  where  account_id=\"%s\""%(money,account_id));
        session.commit();
    else:
        reduce_from="cash_balance";
        LOG.info("#reduce_money in  cash_balance ");
        session.execute("update  account  set  cash_balance=cash_balance-%s  where  account_id=\"%s\""%(money,account_id));
        session.commit();

    session.close();
    LOG.info( "#reduce user=%s money=%s yuan with %s item "%(account_id, money,item));
    return reduce_from;

def get_gift_balance(account_id):
    session=get_mysql_session("billing");
    rows=session.execute('select gift_balance from  account  where account_id=\"%s\"   ;'%account_id).fetchall();
    assert(len(rows)<=1);
    session.close();

    if len(rows)==0:
		return 0;
    else:
    	return rows[0]['gift_balance'];


def get_credit_line(account_id):
    session=get_mysql_session("billing");
    rows=session.execute('select credit_line from  account  where account_id=\"%s\"   ;'%account_id).fetchall();
    assert(len(rows)<=1);
    session.close();
    return rows[0]['credit_line'];

def set_credit_line(account_id,count):
    session=get_mysql_session("billing");
    session.execute("update  account  set  credit_line=%s  where  account_id=\"%s\""%(count,account_id));
    session.commit();
    session.close();

def get_cash_balance(account_id):
    session=get_mysql_session("billing");
    rows=session.execute('select cash_balance from  account  where account_id=\"%s\"   ;'%account_id).fetchall();
    assert(len(rows)<=1);
    session.close();
    return rows[0]['cash_balance'];


def add_cash_balance(uuid,money):
    session = get_mysql_session("billing");
    session.execute("update  account  set  cash_balance=cash_balance+%s  where  account_id=\"%s\""%(money,uuid));
    session.commit();


def reset_cash_balance(uuid,money):
    session = get_mysql_session("billing");
    session.execute("update  account  set  cash_balance=%s  where  account_id=\"%s\""%(money,uuid));
    session.commit();


def reset_gift_balance(uuid,money):
    session = get_mysql_session("billing");
    session.execute("update  account  set  gift_balance=%s  where  account_id=\"%s\""%(money,uuid));
    session.commit();


def add_gift_balance(uuid,money):
    session = get_mysql_session("billing");
    session.execute("update  account  set  gift_balance=gift_balance+%s  where  account_id=\"%s\""%(money,uuid));
    session.commit();

def dump_money():
    session = get_mysql_session("billing");
    for row in session.execute('select * from  account   ;').fetchall():
        row=dict(zip(row.keys(), row.values()));
        account_id=row['account_id'];
        username=row['username'];
        cash_balance=row['cash_balance'];
        gift_balance=row['gift_balance'];
        type=row['type'];
        credit_line=row['credit_line'];
        status=row['status'];
        created_at=row['created_at'];
        updated_at=row['updated_at'];

        print ("account_id:%s|username:%s|cash_balance:%s|gift_balance:%s|type:%s|credit_line:%s|status:%s|created_at:%s|updated_at:%s|\n" %(account_id, username, cash_balance, gift_balance, type, credit_line, status, created_at, updated_at ));


def test_reduce_money():
    from price import  get_cpu_price;
    from get_cpu import  get_cpu_count;

    price=get_cpu_price();
    for user in get_account_ids():
        #count=  get_cpu_count(user_id);
        count=  50;
        money=price*count;
        item="cpu_1_core";
        money="%f"%money;
        print "cpu_core begen to  payment %s with %s\n"%(money, item); 
        
        user_id=str(user);
        reduce_money(user_id,money, item);

def test_reset_cash_balance():
    from price import  get_cpu_price;
    from get_cpu import  get_cpu_count;

    price=get_cpu_price();
    for user in get_account_ids():
        user_id=str(user);
        reset_cash_balance(user_id,1000);

def test_reset_gift_balance():
    from price import  get_cpu_price;
    from get_cpu import  get_cpu_count;

    price=get_cpu_price();
    for user in get_account_ids():
        user_id=str(user);
        reset_gift_balance(user_id,1);

def test_set_credit_line():
    from price import  get_cpu_price;
    from get_cpu import  get_cpu_count;

    price=get_cpu_price();
    for user in get_account_ids():
        user_id=str(user);
        set_credit_line(user_id,2000);

        
#add_gift_balance(user_id, money);

def test_add_gift_balance():
    from price import  get_cpu_price;
    from get_cpu import  get_cpu_count;

    for user in get_account_ids():
        print "add_gift money %s =1 yuan "%user;
        print "Before add gift_balance: %s"%get_gift_balance(user);
        add_gift_balance(user,"1");
        print "After  add gift_balance: %s"%get_gift_balance(user);

def test_add_cash_balance():
    from price import  get_cpu_price;
    from get_cpu import  get_cpu_count;
    import random;

    for user in get_account_ids():
        print "add_gift money %s =1 yuan "%user;
        print "Before add gift_balance: %s"%get_cash_balance(user);
        #add_cash_balance(user,int (random.uniform(0,100)));
        add_cash_balance(user,100);
        print "After  add gift_balance: %s"%get_cash_balance(user);





if __name__=="__main__":
    from logger             import  log_init;

    log_init();

    dump_money();

    test_add_gift_balance();
    test_add_cash_balance();
    test_reduce_money();
    test_reset_cash_balance();
    test_reset_gift_balance();

    test_set_credit_line();

