from kombu import Exchange,Producer
from collecter.rabbitmq.connect import *
from oslo.config import cfg
CONF=cfg.CONF

from producer  import  send_msg;

if __name__=="__main__":
    region_opts = [
        cfg.StrOpt('region_id',
                   default='RegionOne',
                   help=''),
    ]
    CONF = cfg.CONF
    CONF.register_opts(region_opts)
    send_msg({"using_id":"02ae0afa-3667-4927-ba85-2b515268c0ae"})

