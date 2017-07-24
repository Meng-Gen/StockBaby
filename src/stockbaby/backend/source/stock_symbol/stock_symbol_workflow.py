#-*- coding: utf-8 -*-

from stockbaby.backend.workflow.workflow import Workflow
from stockbaby.backend.workflow.task_status import TaskStatus

class StockSymbolWorkflow(Workflow):
    def __init__(self, trigger_datetime):
        self.__trigger_datetime = trigger_datetime
        self.__tasks = [
            StockSymbolSpiderTask(trigger_datetime),
            StockSymbolIngestionTask(trigger_datetime),
        ]

    def get_trigger_datetime(self):
    	return self.__trigger_datetime

    def get_tasks(self):
    	return self.__tasks

class StockSymbolSpiderTask():
    def __init__(self, trigger_datetime):
        self.trigger_datetime = trigger_datetime
        self.curr_status = TaskStatus.READY

    def run(self):
        self.__check_prerequisite()

        self.curr_status = TaskStatus.IN_PROGRESS
        # Crawl
        # If failed, log error to database

        # Else, ENDED
        self.curr_status = TaskStatus.ENDED

    def __check_prerequisite(self):
        pass

class StockSymbolIngestionTask():
    def __init__(self, trigger_datetime):
        self.trigger_datetime = trigger_datetime
        self.curr_status = TaskStatus.READY

    def run(self):
        self.__check_prerequisite()

        self.curr_status = TaskStatus.IN_PROGRESS
        # Crawl
        # If failed, log error to database

        # Else, ENDED
        self.curr_status = TaskStatus.ENDED

    def __check_prerequisite(self):
    	# StockSymbolSpiderTask should be done 
    	# If StockSymbolSpiderTask is not done, log error to database
        self.curr_status = TaskStatus.ERROR
