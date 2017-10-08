import sys; 
sys.path.append("../collecter/")
sys.path.append("../")

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

from    get_last_hour   import  get_last_hour; 
from    tools           import  get_uuid, get_region;
from    billing_resource    import  save_to_resource_mq_buffer_pconn;
from    using               import  save_to_using_mq_buffer_pconn;
from    mysql_db        import  get_mysql_session;
from    get_cdn_user    import  get_all_domains_in_cdn;
from    get_domain_flows  import  get_onedomain_lastmonth_cdnflows, get_onedomain_lastday_bandwidth;



def get_cdn_resource_data():
    domains=get_all_domains_in_cdn();
    ret=[];
    for each in  domains: 
        domain_id=each['domain_id'];
        header={};
        header['hour']=get_last_hour();
        header['id']= domain_id;
        header['user_id']="user_id"
        header['account_id']="user_id"
        header['project_id']=each['tenant_id'];
        header['uuid']="uuid";      
        header['region_id']=get_region();
        header['parent_id']=None;

        ret=[];
        tmp={};
        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();
        amount= get_onedomain_lastmonth_cdnflows(domain_id);

        tmp['cdnflow_1_G']=amount;
        tmp['resource_name']="cdnflow";
        tmp['resource_type']="cdnflow";
        tmp['sum']=amount;
        tmp['billing_item']="cdnflow_1_G";
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);

        tmp={};
        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();
        amount= get_onedomain_lastday_bandwidth(domain_id);
        tmp['cdnbandwidth_1_M']=amount;
        tmp['resource_name']="cdnbandwidth";
        tmp['resource_type']="cdnbandwidth";
        tmp['sum']=amount;
        tmp['billing_item']="cdnbandwidth_1_M";
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);
    
    return ret;



from send_message import   send_mq_message_pconn,get_mq_connection;

from kombu import Connection, Producer, Exchange, Queue

if __name__=="__main__":
    (connection,exchange)=get_mq_connection();

    global count;
    count=0
    session=get_mysql_session("using");
    cdn_resource=get_cdn_resource_data();
    for each in  cdn_resource:
        print each;

        count=count+1;
        send_mq_message_pconn(connection,exchange,each);
        save_to_resource_mq_buffer_pconn(session,each);
        save_to_using_mq_buffer_pconn(session, each['mq_uuid'], each['resource_id']);
        if count%1024 ==0:
            session.commit();

