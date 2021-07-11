import os,tweet
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import random

sched = BlockingScheduler()

if __name__ == '__main__':
    #sched.add_job(tweet.main, 'interval', seconds=10)
    #sched.add_job(tweet.main, 'interval', minutes=1)

    sched.add_job(tweet.main, 'interval', hours=3)
    sched.start()

    