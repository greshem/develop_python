#!/usr/bin/python
#coding:gbk 

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

def  get_tables(session):
    row=session.execute('show tables;   ;').fetchall();
    return row

#处理一个表:
def  deal_with_one_table(name,session):
    #str=name._row[0];
    #str.encode();
    #print "%s"%str;
    str=get_table_name(name);
    table={}; 
    desc=session.execute("desc %s;"%str);
    for field in desc:
        print "\t%s"%field[0];
        table[field[0]]=1;
    return table;
    
#FIXME: 对象的获取 以及 比较  sqlalchemy.engine.result.RowProxy 有问题 Y?      
def get_table_name(row_proxy):
    #if type(row_proxy) !=  'sqlalchemy.engine.result.RowProxy':
        #return None;
    str=row_proxy._row[0];
    str.encode();
    return str;


#dump出一个数据库 的所有的包的字段. 返回 dict of dict 
def dump_one_database():
    DB_CONNECT_STRING = 'mysql+mysqldb://root:password@192.168.210.31/nova?charset=utf8'
    engine = create_engine(DB_CONNECT_STRING, echo=False)
    DB_Session = sessionmaker(bind=engine)
    session2 = DB_Session()

    tables=get_tables(session2);
    ret_db={};
    for each in  tables:
        table=deal_with_one_table(each,session2);
        key=get_table_name(each);
        ret_db[key]=table;

    return ret_db;


if __name__=="__main__":
    ret_db=dump_one_database();
    for key in  ret_db:
        print "#==================================\n";
        print "%s"%key;
        print "%r"%ret_db[key];

