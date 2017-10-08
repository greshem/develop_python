from kombu import Connection, Exchange, Queue, Consumer, eventloop
from pprint import pformat
from json               import * ;
from send_message       import  get_mq_connection_ack,send_mq_message_ack_pconn;
from resend    import  get_resending_resource_ids; 
from mysql_db  import  get_mysql_session;


def test_with_myql():
    session=  get_mysql_session("using");

    resend = get_resending_resource_ids(session);

    for each in  resend:
        msg={};
        print "%s is done "%each['using_id'];
        msg['using_id']=each["using_id"];
        (connection, exchange)=get_mq_connection_ack();
        send_mq_message_ack_pconn(connection,exchange,msg);



def handle_message(body, message):
    global count;
    global  g_connection;
    global  g_exchange;
    count=count+1;
    #print(' Received message: %d %r' % (count,body ));
    message.ack()
    msg={};
    if body.has_key("using_id"):
        msg['using_id']=body["using_id"];
        send_mq_message_ack_pconn(g_connection,g_exchange,msg);


(g_connection, g_exchange)=get_mq_connection_ack();
if __name__=="__main__":
    #log_init();

    global count;
    count=0
    from  send_message  import get_mq_connection;

    #with Connection('amqp://guest:guest@192.168.210.31:5672//') as connection:
    connection, exchange= get_mq_connection();
    queue = Queue('billing_collector', exchange, routing_key='billing_collector')
    with  connection:
        with Consumer(connection, queue, callbacks=[handle_message]):
            for _ in eventloop(connection):
                pass
