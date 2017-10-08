from kombu import Connection, Exchange, Queue, Consumer, eventloop
from pprint import pformat
from json               import * ;
from mq_buffer   import  delete_message, delete_message_pconn;
from mysql_db  import  get_mysql_session;

def handle_message( body, message):
    global count;
    global session;
    count=count+1;
    
    print ('Received message: %d %r' % (count,body ));
    using_id=body['using_id']

    session.execute("update  using.using  set  tran_status=\"delete\"  where using_id=\"%s\""%using_id);
    session.commit();
    message.ack()

def get_mq_server():
    import ConfigParser;
    config_read = ConfigParser.RawConfigParser()
    config_read.read('config.ini')
    server=config_read.get('global','rabbit_mq')
    return server;


session= get_mysql_session("using"); 
if __name__=="__main__":
    exchange = Exchange('billing_collector_ack', type='direct')
    queue = Queue('billing_collector_ack', exchange, routing_key='billing_collector_ack')

    global count;
    count=0
    server=get_mq_server();
    with Connection('amqp://guest:guest@%s:5672//'%server) as connection:
        with Consumer(connection, queue, callbacks=[handle_message]):
            for _ in eventloop(connection):
                pass
