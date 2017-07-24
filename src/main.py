#-*- coding: utf-8 -*-

from stockbaby.backend.source.stock_symbol.stock_symbol_schedule import StockSymbolSchedule

import sys 

def main():
    schedule = StockSymbolSchedule()

    workflow = schedule.create_new_workflow()
    print(workflow.get_trigger_datetime())
    #print(workflow.get_tasks())
    for task in workflow.get_tasks():
        task.run()

if __name__ == '__main__':
    sys.exit(main())

