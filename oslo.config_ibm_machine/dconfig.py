#! /usr/bin/env python
import sys
#from oslo.config import cfg
from oslo_config import cfg

general_opts = [
	cfg.StrOpt('model', default='Compatible PC', help = 'name of the computer')
]

cpu_opts = [
	cfg.StrOpt('name', default='i5', help='cpu model name'),
	cfg.StrOpt('arch', default='x86', help='cpu architecture'),
	cfg.ListOpt('features', default=['apic', 'pae', 'vmx'], help='cpu features'),
	cfg.StrOpt('manufacturer', default='intel', help='cpu manufacturer intel amd etc.'),
	cfg.FloatOpt('frequency', default=2.0, help='cpu frequency in GHz'),
	cfg.IntOpt('cores', default=2, help='number of cpu cores')
]

mem_opts = [
	cfg.IntOpt('frequency', default=1600, help='memory frequency in MHz'),
	cfg.IntOpt('capacity', default=2, help='capacity of the memory in GB'),
	cfg.StrOpt('type', default='ddr3', help='type of the memory ddr2 or ddr3'),
	cfg.BoolOpt('use_ecc', default=False, help='ECC enabled')
]

disk_opts= [cfg.MultiStrOpt('volume', default='WD 500GB', help='disk volumes in GB')]

CONF = cfg.CONF

CONF.register_opts(general_opts)
CONF.register_opts(cpu_opts, 'cpu')
CONF.register_opts(mem_opts, 'mem')
CONF.register_opts(disk_opts, 'disk')

if __name__ == '__main__':
	CONF(sys.argv[1:])

	print '------General Information------'
	print 'Model:', CONF.model

	print '--------CPU---------'
	print 'CPU:', CONF.cpu.name
	print 'cores:', CONF.cpu.cores
	print 'architecture:', CONF.cpu.arch
	print 'features:', CONF.cpu.features
	print 'manufacturer:', CONF.cpu.manufacturer
	print 'frequency:', CONF.cpu.frequency

	print '--------Memory-------'
	print 'capacity:', CONF.mem.capacity
	print 'type:', CONF.mem.type
	print 'frequency:', CONF.mem.frequency
	print 'ECC:', CONF.mem.use_ecc
	
	print '--------Disk---------'
	print 'volumes:', CONF.disk.volume
	# we can change the config in runtime with the set_override
	CONF.set_override('cores',64, 'cpu')
	print 'Ocores:', CONF.cpu.cores	
