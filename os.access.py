#!/usr/bin/python
import os, sys

# Assuming /tmp/foo.txt exists and has read/write permissions.

ret = os.access("/tmp/foo.txt", os.F_OK)
print "F_OK - return value %s"% ret

ret = os.access("/tmp/foo.txt", os.R_OK)
print "R_OK - return value %s"% ret

ret = os.access("/tmp/foo.txt", os.W_OK)
print "W_OK - return value %s"% ret

ret = os.access("/tmp/foo.txt", os.X_OK)
print "X_OK - return value %s"% ret
This produces following result:

F_OK - return value True R_OK - return value True W_OK - return value True X_OK - return value False
