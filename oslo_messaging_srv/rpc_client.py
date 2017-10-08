#! /usr/bin/env python

import sys

from oslo_config import cfg 
#from oslo import messaging
import oslo_messaging  as  messaging

import logging
import datetime

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='rpc_client.log',
                filemode='w')

CONF = cfg.CONF

default_config_file = './msg.conf'

if len(sys.argv) < 2:

	CONF(['--config-file', default_config_file])
	print 'using config file:', default_config_file

transport = messaging.get_transport(cfg.CONF)
target = messaging.Target(topic='demoservice')
client = messaging.RPCClient(transport, target)

if __name__ == '__main__':
	while True:
		context = {'variableA':'HAHA'}
		words = raw_input("input msg to send: ")
		# change call/cast, or the arguments in prepare()(below following argument keywords)
		# exchange, topic, namespace, version, server, fanout, timeout, version_cap
		print 
		print client.prepare(fanout=False).call(context, 'echo',  msg = words, sentime = str(datetime.datetime.now()))
		print
