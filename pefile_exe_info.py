#!/usr/bin/python
import os
import pefile
import time

pe=pefile.PE("/tmp/a.exe");
print pe.dump_info();

