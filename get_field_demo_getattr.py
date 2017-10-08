import exceptions;

class CommandError(Exception):
    message="comman error";
    pass
    




def get_field(item, field):
    try:
        if isinstance(item, dict):
            return item[field]
        else:
            return getattr(item, field)
    except Exception as e:
        msg = "Resource doesn't have field %s"
        #print e.__dict__;
        print "FFFF:%s"%e;
        raise CommandError(msg % field)


import os;
#a=get_field(os, "dup");
body = {'vip': {'name': 'name',
'description': 'description',
'subnet_id': 'subnet_id',
'protocol_port': 'protocol_port',
'protocol': 'protocol',
'pool_id': 'pool_id',
'session_persistence': 'session_persistence',
'admin_state_up': 'admin_state_up'
}}

a=get_field(os, "uname");
print a();

a=get_field(body, "vip");
print a;
