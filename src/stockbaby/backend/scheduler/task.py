#-*- coding: utf-8 -*-

from stockbaby.backend.scheduler.task_status import TaskStatus

class Task():
    def __init__(self, 
                 target=None, 
                 time_period=None, 
                 task_status=None,
                 task_details=None,
                 create_time=None,
                 update_time=None):
        self.target = target
        self.time_period = time_period
        self.task_status = task_status
        self.task_details = task_details
        self.create_time = create_time
        self.update_time = update_time
