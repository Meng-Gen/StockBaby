#-*- coding: utf-8 -*-

from enum import Enum

class TaskStatus(Enum):
    READY = 1
    IN_PROGRESS = 2
    ENDED = 3
    ERROR = 4