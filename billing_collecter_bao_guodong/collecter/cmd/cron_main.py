# -*- coding:utf-8 -*-
'''
Created on 2015-09-01

@author: baoguodong.kevin
'''
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from collecter import config

from oslo.config import cfg
from oslo_log import log
from collecter.collect.collect import collectData
from collecter.message.send_handle import send_data_msg


import datetime


region_opts = [
    cfg.StrOpt('region_id',
               default='RegionOne',
               help=''),
]
CONF = cfg.CONF
CONF.register_opts(region_opts)

def tick():
    print('Tick! The time is: %s' % datetime.datetime.now())
    
def collectInstance():
    collectData("instance")

def collectDisk():
    collectData("disk")
    
def collectSnapshot():
    collectData("snapshot")

def collectRouter():
    collectData("router")

def collectIp():
    collectData("ip")

def collectImage():
    collectData("image")

def collectVpn():
    collectData("vpn")



def main():
    config.parse_args()
    executors = {    
                 'default': ThreadPoolExecutor(10),
                 'processpool': ProcessPoolExecutor(3)
                 }
    job_defaults = {    
                    'coalesce': True,
                    'max_instances':2,
                    'misfire_grace_time':3600
                    }
    scheduler = BlockingScheduler(executors=executors, job_defaults=job_defaults,timezone="UTC")
#    scheduler.add_executor('processpool')
    scheduler.add_jobstore('sqlalchemy', url=CONF.database.connection)
    print CONF.database.connection
    scheduler.add_job(tick, 'interval', seconds=10,id="abcdefg")
#        scheduler.add_job(tick, 'cron', day='2,7,10,15',id="bill_generation")
    scheduler.get_job("get_instance_by_hour") or scheduler.add_job(collectInstance, 'cron', hour='*', id="get_instance_by_hour")
    scheduler.get_job("get_disk_by_hour") or scheduler.add_job(collectDisk, 'cron', hour='*', id="get_disk_by_hour")
    scheduler.get_job("get_snapshot_by_hour") or scheduler.add_job(collectSnapshot, 'cron', hour='*', id="get_snapshot_by_hour")
    scheduler.get_job("get_router_by_hour") or scheduler.add_job(collectRouter, 'cron', hour='*', id="get_router_by_hour")
    scheduler.get_job("get_ip_by_hour") or scheduler.add_job(collectIp, 'cron', hour='*', id="get_ip_by_hour")
    scheduler.get_job("get_image_by_hour") or scheduler.add_job(collectImage, 'cron', hour='*', id="get_image_by_hour")
    scheduler.get_job("get_vpn_by_hour") or scheduler.add_job(collectVpn, 'cron', hour='*', id="get_vpn_by_hour")
    scheduler.get_job("send_data_msg") or scheduler.add_job(send_data_msg, 'cron', minute='*/2', id="send_data_msg")
#        print help(scheduler)
    scheduler.start()

if __name__ == '__main__':
    main()
