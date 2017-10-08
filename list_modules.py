#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pkgutil
def nova_sub_modules():
    for each in pkgutil.iter_modules ('/usr/lib/python2.7/site-packages/nova/',  ""):
        print each; 

nova_sub_modules();
