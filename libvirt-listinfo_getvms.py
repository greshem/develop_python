#!/usr/bin/python
#
#    Munin plugin for libvirt
#
#    Copyright (C) 2008 Canonical Ltd.
#
#	 Authors:
#    Julien Rottenberg
#    Steven Wagner
#    Soren Hansen <soren@canonical.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import libvirt
import re
import sys
from os import environ as env

# Default settings
force_order = []
uri = 'qemu:///system'
graph_type = 'stacked'

# Get overrides from environment
for key in ['force_order', 'uri', 'graph_type']:
    if key in env:
        locals()[key] = eval(env[key], None)

def canonicalise(s):
    return (re.sub('[^A-Za-z_]', '_', s[0]) +
            re.sub('[^0-9A-Za-z_]', '_', s[1:]))

conn = libvirt.openReadOnly(uri)

if conn == None:
    print 'Failed to open connection to the hypervisor'
    sys.exit(1)

try:
    (model, memory, cpus, mhz, nodes, socket, cores, threads) = conn.getInfo()
except:
    print 'getInfo failed'
    sys.exit(1)

#print
#print "KVM running on %d %s %d mhz CPUs w/ %d MB RAM." % (cpus, model, mhz, memory)
#print

active_ids = conn.listDomainsID()
inactive_names = conn.listDefinedDomains() # inactive_names = []
all_domains = [conn.lookupByID(a) for a in active_ids] + [conn.lookupByName(a) for a in inactive_names]

def domsort(adom, bdom):
    a = adom.name()
    b = bdom.name()
    if a in force_order and b not in force_order:
        return -1
    if b in force_order and a not in force_order:
        return 1
    if a in force_order and b in force_order:
        return force_order.index(a) - force_order.index(b) 
    return cmp(a, b)

all_domains.sort(domsort)

if len(all_domains) == 0:
    print 'No domains found.'
    sys.exit(1)

if len(sys.argv) == 2:
    if sys.argv[1] == "config":
        print "graph_title KVM Domain CPU Utilization"
        print "graph_vlabel CPU use in microseconds"
        print "graph_args --base 1000"
        print "graph_category Virtual Machines"

        first = True
        for dom in all_domains:
            nodeName = dom.name()
            canon_name = canonicalise(nodeName)
            if graph_type == 'stacked':
                print "%s.draw %s" % (canon_name, ['STACK', 'AREA'][first])
            else:
                print "%s.draw LINE1" % canon_name
            print "%s.type DERIVE" % canon_name
            print "%s.min 0" % canon_name
            print "%s.label %s" %(canon_name, nodeName)
            first = False
        sys.exit(0)
        
for dom in all_domains:
    state, maxMem, memory, numVirtCpu, cpuTime = dom.info()
    nodeName = dom.name()
#    uuid = dom.UUID()
#    ostype = dom.OSType()
#    print """Domain: %s, %s state (%s), %d CPUs, %d seconds, %d milliseconds, mem/max (%d/%d) """ \
#          % (nodeName, ostype, state, numVirtCpu, cpuTime/float(1000000000), cpuTime/float(1000000), memory, maxMem )
# rrdtool will only do "DERIVED" when the data type is integer
    print "%s.value %d" % (canonicalise(nodeName), cpuTime/float(1000))


