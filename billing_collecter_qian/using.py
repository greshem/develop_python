#!/usr/bin/python  
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from mysql_db import  get_mysql_session;
from billing_resource   import  get_billing_resource_id_all;
from random import choice

def save_to_using_mq_buffer_pconn(session,mq_id,resource_id):
    if session == None: 
        session=get_mysql_session("using");
    #session.execute("use using"); FIXME, using is keyword in sql
    sql_str="""
INSERT delayed  INTO `using`.`using` (`using_id`, `resource_id`, `created_at`, `started_at`, `ended_st`, `tran_status`) VALUES ("%s", "%s", CURRENT_TIMESTAMP, NULL, NULL, "%s");
""" %(mq_id, resource_id, "sending");
    #print sql_str;
    session.execute(sql_str);
    #session.commit();

        


def save_to_using_mq_buffer(mq_id,resource_id):

    session=get_mysql_session("using");
    save_to_using_mq_buffer_pconn(session,  mq_id, resource_id);
    session.close();

def test_insert():
    all_ids= get_billing_resource_id_all();
    for each in all_ids:
        save_to_using_mq_buffer(each, each);
    

def dump():
    session = get_mysql_session("using");
    for row in session.execute('select * from  using.using   ;').fetchall():
        row=dict(zip(row.keys(), row.values()));
        using_id=row['using_id'];
        resource_id=row['resource_id'];
        created_at=row['created_at'];
        started_at=row['started_at'];
        ended_st=row['ended_st'];
        tran_status=row['tran_status'];


        print "using_id=%s\n"%using_id,
        print "resource_id=%s\n"%resource_id,
        print "created_at=%s\n"%created_at,
        print "started_at=%s\n"%started_at,
        print "ended_st=%s\n"%ended_st,
        print "tran_status=%s\n"%tran_status,


if __name__=="__main__":
    dump();
    #save_to_using_mq_buffer();
