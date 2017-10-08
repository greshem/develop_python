
#import logging


def oslo_log_test():
    from oslo_log import log as logging
    LOG = logging.getLogger(__name__)
    LOG.info('1.This is info message')
    LOG.warning('2. This is warning message')
    LOG.error('3. This is ERROR message')
    LOG.debug('4.This is debug message')


#DEBUG INFO 
def  log_init():
    import logging
    import os
    FILE=os.getcwd()

    #format='%(asctime)s:%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    logging.basicConfig(level=logging.INFO,
                        datefmt='[%Y %H:%M:%S]',
                        filename = os.path.join(FILE,'all.log'),
                        filemode='a+')

    formatter = logging.Formatter('%(levelname)s [%(asctime)s] [%(name)s]:%(pathname)s line=%(lineno)d [message="%(message)s"]')
    logging.info('log system init')

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    #logging.addHandler(ch)

    #logging.debug(msg)

if __name__=="__main__":
    log_init();
    oslo_log_test();
