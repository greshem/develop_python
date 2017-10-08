#!/usr/bin/python 

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from mysql_db    import   get_mysql_session;

def add_discount_record():
    session = get_mysql_session("billing");
    account_id="account_id";
    rows=session.execute('insert discount values ( 222, 1, "%s", 0.77, null, null )  ;'%account_id);
    session.close();

def get_account_user_id():
    session = get_mysql_session("billing");
    rows=session.execute('select distinct  account_id  from  account; ').fetchall();
    tenant_list = [i['account_id'] for i in rows]
    return tenant_list;


def get_discount_with(account_id,billing_item_id):
    session = get_mysql_session("billing");
    rows=session.execute('select * from  discount where  account_id=\"%s\" and  billing_item_id=\"%s\";'%(account_id,billing_item_id)).fetchall();
    discount_ratio=1;
    assert( len(rows)<= 1);
    for row in       rows:
        row=dict(zip(row.keys(), row.values()));
        #discount_id=row['discount_id'];
        #billing_item_id=row['billing_item_id'];
        #account_id=row['account_id'];
        discount_ratio=row['discount_ratio'];
        #created_at=row['created_at'];
        #updated_at=row['updated_at'];
    session.close();
    return discount_ratio;

def get_discount():
    session = get_mysql_session("billing");
    rows= session.execute('select * from  discount ;').fetchall();
    for row in rows:
        row=dict(zip(row.keys(), row.values()));
        #discount_id=row['discount_id'];
        #billing_item_id=row['billing_item_id'];
        #account_id=row['account_id'];
        discount_ratio=row['discount_ratio'];
        #created_at=row['created_at'];
        #updated_at=row['updated_at'];
    session.close();
    return float(discount_ratio);

if __name__=="__main__":
    #add_discount_record();
    #print get_discount();
    #users=get_account_user_id();
    users=get_account_user_id();
    for each in  users:
        discount=get_discount_with(each,1)
        print "%s == %f"%(each,  discount);

    assert (get_discount_with("user_not_exists",1) == 1);
