import random

def getWaitLoadingTime():
    WAIT_TIME = random.uniform(3, 5)
    return WAIT_TIME

def getWaitScrollTime():
    WAIT_TIME = random.uniform(1, 3)
    return WAIT_TIME

def getWaitScrollTimeFast():
    WAIT_TIME = random.uniform(0.1, 0.5)
    return WAIT_TIME

def getWaitInTargetWithDetailTime():
    WAIT_TIME = random.uniform(1, 4)
    return WAIT_TIME

def getWaitInTargetTime():
    WAIT_TIME = random.uniform(3, 6)
    return WAIT_TIME
