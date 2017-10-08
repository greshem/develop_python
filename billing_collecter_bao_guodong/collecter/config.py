# -*- coding:utf-8 -*-
'''
Created on 2015年9月22日

@author: baoguodong.kevin
'''
from oslo_log import log
from oslo.config import cfg
from collecter.db.sqlalchemy import session
CONF=cfg.CONF
LOG = log.getLogger(__name__)

def parse_args():
    log.register_options(CONF)
    CONF([],
         project='conllecter',
         version='v1.0',
         default_config_files=['../../etc/collecter.conf'])
    log.setup(CONF, "conllecter")