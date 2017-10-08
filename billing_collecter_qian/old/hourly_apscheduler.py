"""
Demonstrates how to schedule a job to be run in a process pool on 3 second intervals.
"""

from datetime import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler

#from  get_last_hour   import   append_this_hour is_in_history_hour get_last_hour


def tick():
    global producer;
    print('Tick! The time is: %s' % datetime.now())


global producer;
if __name__ == '__main__':

    from kombu import Connection, Producer, Exchange, Queue
    exchange = Exchange('billing_collector', type='direct')
    queue = Queue('billing_collector', exchange, routing_key='billing_collector')

    connection=Connection('amqp://guest:guest@192.168.210.31:5672//');
    producer = Producer(connection);

    scheduler = BlockingScheduler()
    scheduler.add_executor('processpool')
    scheduler.add_job(tick, 'interval', seconds=4)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
