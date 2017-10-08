#!/usr/bin/python
from rhpl import *
import rhpl
#import rhpl.comps
import sys

comps = rhpl.comps.Comps(sys.argv[1])
for group in comps.groups.values():
    pkgs = []
    for (type, pkg) in group.packages.values():
        if type == u'mandatory':
            pkgs.append(pkg)
    print group.name, pkgs
