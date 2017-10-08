#!/usr/bin/python  


from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

import sys;
sys.path.append("../");

from mysql_db  import get_mysql_session;
from accountDao_test  import  add_one_user;
def  add_one_user2(session, id, name ):	
		account_id=row['account_id'];
        username=row['username'];
        cash_balance=100;
        gift_balance=200;
        type=;
        credit_line=2000;
        status=;
        created_at=row['created_at'];
        updated_at=row['updated_at'];
			


session = get_mysql_session("keystone");
for row in session.execute('select * from  user   ;').fetchall():
    row=dict(zip(row.keys(), row.values()));
    id=row['id'];
    name=row['name'];

    print "id=%s\n"%id;
    print "name=%s\n"%name;
    add_one_user(id, name);

