#!/usr/bin/python
import os
try:
	st=os.stat("/no_exists");
except os.error:
	print os.error
