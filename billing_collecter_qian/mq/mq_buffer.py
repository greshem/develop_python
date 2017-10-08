#!/usr/bin/python 
#CREATE TABLE mq_buffer(uuid varchar(64), msg varchar(1024),  status  varchar(32),  create_at timestamp , update_at   timestamp  );

import sys;
sys.path.append("../");
from  mysql_db  import  get_mysql_session;
from  tools     import  get_uuid, json_to_dic;
from  send_message  import  get_mq_connection,send_mq_message_pconn;



def save_to_mq_buffer(uuid, msg):
    session= get_mysql_session("using"); 

    session.execute("insert into mq_buffer values(\"%s\",\"%s\" ,\"sending\",NULL, NULL )"%(uuid,msg));

    session.commit();
    session.close();

def make_msg_from_resource_id():
    pass;


def  delete_message(uuid):
    assert(isinstance(uuid, str) or isinstance(uuid, unicode));
    session= get_mysql_session("using"); 

    session.execute("update  using.using  set  tran_status=\"delete\"  where using_id=\"%s\""%uuid);
    session.commit();
    session.close();

def  delete_message_pconn(session,uuid):
    assert(isinstance(uuid, str) or isinstance(uuid, unicode));

    session.execute("update  using.using  set  tran_status=\"delete\"  where using_id=\"%s\""%uuid);
    session.commit();

