import random

def getWaitStartThreadTime():
    return random.uniform(50, 60)

def getWaitLoadingTime():
    return random.uniform(2, 3)

def getWaitScrollTime():
    return random.uniform(1, 2)

def getWaitInTargetWithDetailTime():
    return random.uniform(2, 5)

def getWaitInTargetTime():
    return random.uniform(2, 5)

def getWaitImageProductLoadingTime():
    return random.uniform(5, 10)

def getWaitRepeatingTime():
    return random.uniform(25, 30)

def getWaitLoadingTimeForCache():
    return random.uniform(10, 20)

def getWakeWaitingTime():
    return random.uniform(10, 200)