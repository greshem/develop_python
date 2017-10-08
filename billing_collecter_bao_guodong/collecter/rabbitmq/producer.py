# -*- coding:utf-8 -*-
'''
Created on 2015年9月22日

@author: baoguodong.kevin
'''
from kombu import Exchange,Producer
from collecter.rabbitmq.connect import *
from oslo.config import cfg
CONF=cfg.CONF

def send_msg(msg):  
    connection,channel=getChannelAndConnection()
      
    media_exchange = Exchange(CONF.region_id, 'direct', channel)
    
    producer = Producer(channel, exchange=media_exchange, routing_key=CONF.region_id)  
  
    producer.publish(msg)

def send_ack_msg(msg):
    connection,channel=getChannelAndConnection()
      
    exchange = Exchange(CONF.region_id+"_ack", 'direct', channel)
    
    producer = Producer(channel, exchange=exchange, routing_key=CONF.region_id+"_ack")  
  
    producer.publish(msg)

if __name__=="__main__":
    region_opts = [
        cfg.StrOpt('region_id',
                   default='RegionOne',
                   help=''),
    ]
    CONF = cfg.CONF
    CONF.register_opts(region_opts)
    send_ack_msg({"using_id":"02ae0afa-3667-4927-ba85-2b515268c0ae"})
