# -*- coding:utf-8 -*-
'''
Created on 2015年9月22日

@author: baoguodong.kevin
'''
from kombu import Exchange,Producer,Connection,Queue
from oslo.config import cfg

rabbitmq_opts=[
    cfg.StrOpt('connection',
               default='amqp://guest:guest@localhost:5672//',
               help=''),
]
CONF = cfg.CONF
CONF.register_opts(rabbitmq_opts, 'rabbit')


def init():
    '''初始化exchange和queue'''
    connection = Connection(CONF.rabbit.connection)  
    channel = connection.channel()  
    exchange = Exchange(CONF.region_id, 'direct', channel)
    exchange.declare()
    queue = Queue(CONF.region_id, exchange=exchange, routing_key=CONF.region_id, channel=channel) 
    queue.declare()

def init_ack():
    '''初始化返回exchange和queue'''
    connection = Connection(CONF.rabbit.connection)  
    channel = connection.channel()  
    exchange = Exchange(CONF.region_id+'_ack', 'direct', channel)
    exchange.declare()
    queue = Queue(CONF.region_id+'_ack', exchange=exchange, routing_key=CONF.region_id+'_ack', channel=channel) 
    queue.declare()

    
def getChannelAndConnection():
    connection = Connection(CONF.rabbit.connection)
#    connection = Connection(CONF.rabbit.connect)  
    channel = connection.channel()
    return connection,channel
