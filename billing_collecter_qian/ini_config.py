#!/usr/bin/python
# -*- coding:utf-8 -*-
import os;
import ConfigParser



def gen_ini():
    ini = open('config.ini','w')
    config_write = ConfigParser.RawConfigParser()
    config_write.add_section('global')

    config_write.set('global','rabbit_mq','localhost')

    config_write.set('global','mysql_server','localhost')
    config_write.set('global','mysql_user','root')
    config_write.set('global','mysql_password','password')
    
    config_write.set('global','region','regoin_beijing_1')

    config_write.write(ini)
    ini.close()

def ini_get_value(key):
    config_read = ConfigParser.RawConfigParser()
    config_read.read('config.ini')
    return  config_read.get('global',key)

    

def read_ini():
    config_read = ConfigParser.RawConfigParser()
    config_read.read('config.ini')
    print "region=%s"%config_read.get('global','region')
    print "rabbit_mq=%s"%config_read.get('global','rabbit_mq')
    print "mysql_server=%s"%config_read.get('global','mysql_server')
    print "mysql_user=%s"%config_read.get('global','mysql_user')
    print "mysql_passwd=%s"%config_read.get('global','mysql_password')


if __name__ == "__main__":
    if not os.path.isfile('config.ini'):
        gen_ini();
    read_ini();
