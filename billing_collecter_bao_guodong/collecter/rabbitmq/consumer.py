# -*- coding:utf-8 -*-
'''
Created on 2015年9月22日

@author: baoguodong.kevin
'''
from kombu import Exchange, Queue, Consumer
from collecter.rabbitmq.connect import *
from collecter.message.ack_handle import *
from oslo.config import cfg
region_opts=[
    cfg.StrOpt('region_id',
               default='RegionOne',
               help=''),
]

CONF = cfg.CONF
CONF.register_opts(region_opts)


print CONF.region_id;

from oslo_log import log as logging
LOG = logging.getLogger(__name__)
  
  
def process_msg(body, message):  
    print body  
    message.ack()

def process_ack_msg(body, message): 
    LOG.info(body)
    try:
        ack_msg(body)
    except Exception as e:
        LOG.error(str(e))
    finally:  
        message.ack()

 
def consumer_wait():  
    connection, channel = getChannelAndConnection()
    exchange = Exchange(CONF.region_id, 'direct', channel)  
    queue = Queue(CONF.region_id, exchange=exchange, routing_key=CONF.region_id, channel=channel)  
    consumer = Consumer(channel, queues=[queue], callbacks=[process_msg])   
    consumer.consume()  
    while True:  
        connection.drain_events()  
    consumer.cancel()

def consumer_ack_wait():
    connection, channel = getChannelAndConnection()
    exchange = Exchange(CONF.region_id + "_ack", 'direct', channel)  
    queue = Queue(CONF.region_id + "_ack", exchange=exchange, routing_key=CONF.region_id + "_ack", channel=channel)  
    consumer = Consumer(channel, queues=[queue], callbacks=[process_ack_msg])   
    consumer.consume()  
    while True:  
        connection.drain_events()  
    consumer.cancel()  
  
if __name__ == "__main__":
    #consumer_wait()
    consumer_ack_wait()
