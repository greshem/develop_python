# -*- coding:utf-8 -*-
'''
Created on 2015年9月22日

@author: baoguodong.kevin
'''
from oslo.config import cfg
from oslo_log import log as logging
from collecter import config
from collecter.rabbitmq import connect
from collecter.rabbitmq import consumer

LOG = logging.getLogger(__name__)

region_opts = [
    cfg.StrOpt('region_id',
               default='RegionOne',
               help=''),
]
CONF = cfg.CONF
CONF.register_opts(region_opts)

def main():
    config.parse_args()
    connect.init()
    connect.init_ack()
    consumer.consumer_ack_wait()
#    consumer.consumer_wait()

if __name__=="__main__":
    main()
    
    
    
