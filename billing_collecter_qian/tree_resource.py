#!/usr/bin/python  
import sys; 
sys.path.append("collecter/")

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker


from    get_last_hour   import  get_last_hour; 
from    mysql_db        import  get_mysql_session;
from    tools           import  get_uuid, get_region;

from    get_instance    import  get_instance_pconn;
from    get_ip          import  get_ip_count_pconn;
from    get_cpu         import  get_cpu_count_pconn;
from    get_disk        import  get_disks_pconn;
from    get_memory      import  get_memory_count_pconn;
from    get_router      import  get_user_routers_pconn;
from    get_vpn         import  get_vpn_pconn;
from    get_snapshotdisk    import  get_snapshotdisk_pconn;

from    mq_buffer           import  save_to_mq_buffer;
from    billing_resource    import  save_to_resource_mq_buffer_pconn;
from    using               import  save_to_using_mq_buffer_pconn;


 

def  get_resource_data(session):
    print "info: begin to collector data "; 
    last_hour=get_last_hour;
    instances=get_instance_pconn(session); 
    ret=[];
    for each in instances:

        header={};
        
        user_id=each['user_id'];
        project_id=each['project_id'];
        uuid=each['uuid'];


        header['hour']=get_last_hour();
        header['id']=each['id'];  #instance's id 
        header['user_id']=user_id
        header['account_id']=user_id
        header['project_id']=project_id;    
        header['uuid']=uuid;      #instance's uuid 
        header['region_id']=get_region();
        header['parent_id']=None;

       
        #print "UUID=%s, user_id=%s, project_id=%s, id=%s"%(uuid, user_id,project_id, id);
        #print "Cpu_core=%d"%get_cpu_count(uuid);
        #print "Memory=%d"%get_memory_count(uuid);
        tmp={};
        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();
        sum=get_cpu_count_pconn(session,uuid);
        tmp['billing_item']="cpu_1_core";
        tmp['resource_name']="cpu";
        tmp['resource_type']="cpu";
        tmp['cpu_1_core']=sum;
        tmp['sum']=sum;
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);

        tmp={};
        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();

        tmp['billing_item']="instance_1";
        tmp['resource_name']="instance";
        tmp['resource_type']="instance";
        tmp['instance_1']=1;
        tmp['sum']=1;
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);

        tmp={};

        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();

        sum=get_memory_count_pconn(session, uuid);
        tmp['billing_item']="memory_1024_M";
        tmp['resource_name']="memory";
        tmp['resource_type']="memory";
        tmp['memory_1024_M']=int(sum/1024);
        tmp['sum']= int(sum/1024);
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);


        #print "Disk:  ";

        
        tmp={};

        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();
        (sizes,size_amount)=get_disks_pconn(session, user_id, project_id);
        #for each in sizes:
        #    print each;
        tmp['billing_item']="disk_1_G";
        tmp['resource_name']="disk";
        tmp['resource_type']="disk";
        tmp['disk_1_G']=size_amount;
        tmp['sum']=size_amount;
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);


        tmp={};

        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();
        (snapshots, snapshot_size_amount)=get_snapshotdisk_pconn(session, project_id);
        #for each2 in snapshots:
        #    print "\t SNAPSHOT: %s"%each2;
        tmp['billing_item']="snapshotdisk_1_G";
        tmp['resource_name']="snapshotdisk";
        tmp['resource_type']="snapshotdisk";
        tmp['snapshotdisk_1_G']=snapshot_size_amount;
        tmp['sum']=snapshot_size_amount;
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);



        tmp={};

        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();
        #print "Router count=%d"%len(get_user_routers(project_id));
        sum=len(get_user_routers_pconn(session, project_id));
        tmp['billing_item']="router_1";
        tmp['resource_name']="router";
        tmp['resource_type']="router";
        tmp['router_1']=sum;
        tmp['sum']=sum;
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);

        tmp={};

        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();
        #print "Router bandwidth%d"%0;
        sum=0;
        tmp['billing_item']="bandwidth_1_M";
        tmp['resource_name']="bandwidth";
        tmp['resource_type']="bandwidth";
        tmp['sum']=sum;
        tmp['bandwidth_1_M']=sum;
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);

        
        tmp={};

        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();
        #print "Floating IP count=%d"%len(get_ip_count(project_id));
        sum= len(get_ip_count_pconn(session, project_id));

        tmp['ip_1']=sum;
        tmp['resource_name']="ip";
        tmp['resource_type']="ip";
        tmp['billing_item']="ip_1";
        tmp['sum']=sum;
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);


        tmp={};

        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();
        sum=len(get_vpn_pconn(session,project_id));
        tmp['vpn_1']=sum;
        tmp['resource_name']="vpn";
        tmp['resource_type']="vpn";
        tmp['billing_item']="vpn_1";
        tmp['sum']=sum;
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);


        #vpn=get_vpn(project_id);
        #if(len(vpn)==0):
            #print "VPN: \t%s have no vpn settings;"%project_id;
        #    tmp=0;
        #else:
        #     for each2 in vpn:
        #        print "VPN: \t%s"%each2;
        
        #print "CDN: %d"%0;
        tmp={};

        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();
        sum=2;
        tmp['cdnflow_1_G']=sum;
        tmp['resource_name']="cdnflow";
        tmp['resource_type']="cdnflow";
        tmp['sum']=sum;
        tmp['billing_item']="cdnflow_1_G";
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);


        tmp={};

        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();
        sum=2048;
        tmp['cdnbandwidth_1_M']=(sum/1024);
        tmp['resource_name']="cdnbandwidth";
        tmp['resource_type']="cdnbandwidth";
        tmp['sum']=(sum/1024);
        tmp['billing_item']="cdnbandwidth_1_M";
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);


        tmp={};

        header['mq_uuid']=get_uuid();
        header['resource_id']=get_uuid();
        sum=1;
        tmp['image_1']=sum;
        tmp['resource_name']="image";
        tmp['resource_type']="image";
        tmp['sum']=sum;
        tmp['billing_item']="image_1";
        tmp['status']="sending";
        resource=dict(header, **tmp);
        ret.append(resource);

        
        #print resource;
        #ret.append(resource);
    return ret;


from send_message import   send_mq_message_pconn,get_mq_connection;

from kombu import Connection, Producer, Exchange, Queue

if __name__=="__main__":
    (connection,exchange)=get_mq_connection();
    session=get_mysql_session("nova");
    data=get_resource_data(session);
    global count;
    count=0
    for each in data:

        count=count+1;
        print "count=%d, %s"%(count,each);
        send_mq_message_pconn(connection,exchange,each);
        #save_to_mq_buffer(each['mq_uuid'], each);
        save_to_resource_mq_buffer_pconn(session,each);
        save_to_using_mq_buffer_pconn(session, each['mq_uuid'], each['resource_id']);
        if count%1024 ==0:
            session.commit();




