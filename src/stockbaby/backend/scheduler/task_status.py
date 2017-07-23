#-*- coding: utf-8 -*-

from enum import Enum

class TaskStatus(Enum):
    READY = 1
    CRAWLING = 2
    CRAWLED = 3
    INGESTING = 4
    INGESTED = 5
    FINAL = 6
    ERROR = 7
