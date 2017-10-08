#!/usr/bin/python

import os, time, popen2 
#raw_out, raw_in, raw_err = popen2.Popen4("cat /etc/passwd" );    

raw_out, raw_in, raw_err  = popen2.Popen3("cat /etc/passwd" );    
