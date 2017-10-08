# -*- coding: utf-8 -*-

import os
import sys
import errno
import time;

def basic_daemonize():
    # See http://www.erlenstar.demon.co.uk/unix/faq_toc.html#TOC16
    if os.fork():   # launch child and...
        os._exit(0) # kill off parent
    os.setsid()
    if os.fork():   # launch child and...
        os._exit(0) # kill off parent again.
    os.umask(022)   # Don't allow others to write
    null=os.open('/dev/null', os.O_RDWR)
    for i in range(3):
        try:
            os.dup2(null, i)
        except OSError, e:
            if e.errno != errno.EBADF:
                raise
    os.close(null)


def writePID(pidfile):
    open(pidfile,'wb').write(str(os.getpid()))
    if not os.path.exists(pidfile):
        raise Exception( "pidfile %s does not exist" % pidfile )


def checkPID(pidfile):
    if not pidfile:
        return
    if os.path.exists(pidfile):
        try:
            pid = int(open(pidfile).read())
        except ValueError:
            sys.exit('Pidfile %s contains non-numeric value' % pidfile)
        try:
            os.kill(pid, 0)
        except OSError, why:
            if why[0] == errno.ESRCH:
                # The pid doesnt exists.
                print('Removing stale pidfile %s' % pidfile)
                os.remove(pidfile)
            else:
                sys.exit("Can't check status of PID %s from pidfile %s: %s" %
                         (pid, pidfile, why[1]))
        else:
            sys.exit("Another server is running, PID %s\n" %  pid)

def daemonize(pidfile):
    checkPID(pidfile)
    basic_daemonize()
    writePID(pidfile)


def file_append(string):
    fh = open("/tmp/daemon.log", 'a')
    fh.write("%s\n"%( string) )
    fh.close();

def get_cur_time():
        return time.strftime("%Y-%m-%d_%H:%M:%S ",time.localtime())

if __name__ == '__main__':
    daemonize("/tmp/aaaa.pid")
    while 1:
        time.sleep(1);
        file_append(get_cur_time());
