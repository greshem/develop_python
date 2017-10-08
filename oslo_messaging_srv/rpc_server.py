#! /usr/bin/env python
import os
import sys
import logging

from oslo_config import cfg
#from oslo_messaging import messaging
import oslo_messaging as  messaging

import datetime

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='rpc_server.log',
                filemode='w')

CONF = cfg.CONF
config_file_args = ['--config-file', './msg.conf']

class ServerManager(object):
	rid = 0
	def echo(self, ctx, msg, sentime):
		print '%s request msg: %s' % (sentime, msg)
		self.rid = self.rid + 1
		s = '%s server(%d) accepted no.%d' % (datetime.datetime.now(), os.getpid(), self.rid)
		print s
		return s

endpoints = [ServerManager()]


if __name__ == '__main__':
	if len(sys.argv) >= 2:
		config_file_args = sys.argv[1:3]
	CONF(config_file_args)

	transport = messaging.get_transport(CONF)
	target = messaging.Target(topic='demoservice', server='server' + str(os.getpid()))
	server = messaging.get_rpc_server(transport, target, endpoints)
	
	print 'server(%d) starting' % os.getpid()
	server.start()
	server.wait()
	
