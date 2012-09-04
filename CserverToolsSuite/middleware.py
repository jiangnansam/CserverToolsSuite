'''
Created on 2012-8-30

@author: qjwang2
'''
from apscheduler.scheduler import Scheduler
from Cli.service import cli_service

class CtsStartupMiddleware(object):
    
    def __init__(self):
        sched = Scheduler()
        sched.add_cron_job(cli_service.refreshCache, hour=0)
        sched.start()
        
        
