#-*- coding: utf-8 -*-

class TaskManager():
    def run(self):
        print('[Scheduler] Initial')
        StockSymbolScheduler().run()
        print('[Scheduler] Final')

class StockSymbolScheduler():
    def run(self):
        print('[StockSymbolScheduler] Initial')
        print('[StockSymbolScheduler] Task Creating')
        
        print('1. Create new tasks in the specific day')
        print('2. The status of task should be ready')
        print('3. Do not create duplicated tasks')

        #self.goto_final_state()



        print('[StockSymbolScheduler] Final')



Scheduler().run()
