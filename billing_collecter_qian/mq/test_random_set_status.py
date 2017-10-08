#!/usr/bin/python 
from mysql_db import  get_mysql_session;
def get_all_using_id(session):
    if session==None:
        session=get_mysql_session("using");

    rows=session.execute("select *  from   using.using where 1 ;");
    ret= [ each['using_id']    for each in rows ];
    return ret;

if __name__=="__main__":
    from  random   import choice;
    session=get_mysql_session("using");

    ids=get_all_using_id(session);
    for each in  range(1,1024):
        one_id=choice(ids);
        print one_id;
        session.execute("update  using.using set tran_status='sending' where using_id=\"%s\" "%one_id);
        session.commit();
