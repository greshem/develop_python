from kombu import Connection, Producer, Exchange, Queue

server="localhost";
connection=Connection('amqp://guest:guest@%s:5672//'%server) 
channel = connection.channel();

for each in range(1,1024):
    exchange = Exchange("BB_exchange_%s"%each, 'direct', channel)
    exchange.declare()

    queue = Queue("BB_queue_%s"%each, exchange=exchange, routing_key="BBBBBB", channel=channel)
    queue.declare()

