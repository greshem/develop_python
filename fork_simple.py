#coding=utf8
 
import os
import time;
 
#创建子进程之前声明的变量
source = 10
 
try:
    pid = os.fork()
 
    if pid == 0: #子进程
        print "this is child process."
        #在子进程中source自减1
        source = source - 1
        while 1:
            print "loop with child \n";
            time.sleep(3)
    else: #父进程
        print "this is parent process."
 
    print source
except OSError, e:
    pass
