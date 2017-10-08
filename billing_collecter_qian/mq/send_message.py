#coding=gbk
import ConfigParser;


def get_mq_connection():
    config_read = ConfigParser.RawConfigParser()
    config_read.read('config.ini')
    server=config_read.get('global','rabbit_mq')

    from kombu import Connection, Producer, Exchange, Queue

    connection=Connection('amqp://guest:guest@%s:5672//'%server) 
    channel = connection.channel();

    exchange = Exchange("billing_collector", 'direct', channel)
    exchange.declare()

    queue = Queue("billing_collector", exchange=exchange, routing_key="billing_collector", channel=channel)
    queue.declare()

    return(connection, exchange);

def get_mq_connection_ack():
    config_read = ConfigParser.RawConfigParser()
    config_read.read('config.ini')
    server=config_read.get('global','rabbit_mq')

    from kombu import Connection, Producer, Exchange, Queue
    exchange = Exchange('billing_collector_ack', type='direct')
    queue = Queue('billing_collector_ack', exchange, routing_key='billing_collector_ack')
    connection=Connection('amqp://guest:guest@%s:5672//'%server) 
    return(connection, exchange);



def send_mq_message_delete(connection, exchange, msg):
    with  connection:
        producer = Producer(connection)
        #for each in range(1,1024):
        producer.publish(msg,
                 exchange=exchange,
                 routing_key='billing_collector',
                 serializer='json', compression='zlib')



def  send_mq_message_pconn(connection,exchange,msg):
    from kombu import Connection, Producer, Exchange, Queue
    producer = Producer(connection)
    #producer.publish({'MSG': msg},
    producer.publish(msg,
                 exchange=exchange,
                 routing_key='billing_collector',
                 serializer='json', compression='zlib')


def  send_mq_message_ack_pconn(connection,exchange,msg):
    from kombu import Connection, Producer, Exchange, Queue
    producer = Producer(connection)
    #producer.publish({'MSG': msg},
    producer.publish(msg,
                 exchange=exchange,
                 routing_key='billing_collector_ack',
                 serializer='json', compression='zlib')

if __name__=="__main__":
    import sys;
    sys.path.append("../");

    from tools  import  get_uuid, get_region;
    from get_last_hour  import  get_last_hour;
    from account_tools  import  get_all_user;
    from random     import choice;

    #users= get_all_user();
    users=['aa','bb','cc'];
    resource={};
    resource['hour']=get_last_hour();
    resource['id']     ="11100000000000000000000000000001";
    resource['mq_uuid']=get_uuid();
    resource['region_id']=get_region();
    resource['user_id']=choice(users);
    resource['project_id']="project_id";
    resource['uuid']   ="instance000000000000000000000001";
    resource['cpu_1_core']=16;
    resource['instance_1']=1;
    resource['memory_1024_M']=(4096/1024); #FIXME  /1024, 这里是硬代码, 
    resource['disk_1_G']= 100;
    resource['snapshotdisk_1_G']=100;
    resource['router_1']=3;
    resource['bandwidth_1_M']=0;
    resource['ip_1']=4;
    resource['vpn_1']=4;
    resource['cdnflow_1_G']=2;
    resource['cdnbandwidth_1_M']=(2048/1024); #FIXME  /1024, 这里也是硬代码, 
    resource['image_1']=1;

    resource['billing_item']="vpn_1"; 

    (connection, exchange)=get_mq_connection();
    for each in range(1,1024):
        send_mq_message_pconn(connection,exchange, resource);

    print "send ok ";
