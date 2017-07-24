#-*- coding: utf-8 -*-

from stockbaby.backend.workflow.schedule import Schedule
from stockbaby.backend.source.stock_symbol.stock_symbol_workflow import StockSymbolWorkflow

from croniter import croniter
from datetime import datetime

class StockSymbolSchedule():
    def __init__(self):
        self.cron = croniter('0 0 * * *', datetime.now()) 

    def create_new_workflow(self):
        trigger_datetime = self.cron.get_next(datetime)
        return StockSymbolWorkflow(trigger_datetime=trigger_datetime)

#    def get_cron_next_value(self):
#        return self.cron.get_next(datetime)
