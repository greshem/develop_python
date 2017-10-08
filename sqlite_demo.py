

import random;
import sqlite3
con=sqlite3.connect("/tmp/test2.db");

cursor = con.cursor()

def create_table_and_data(con):
    con.execute("create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)")

    for each in range(1,100):
            num= random.randint(10000,1000000);
            t=(num,num, "tset2%s"%each, "test2%s"%each); 
            #print t;
            con.execute("insert into catalog values (?,?,?,?)", t)

    con.commit();



cursor.execute("select * from catalog")
for each in cursor.fetchall():
    print each;
