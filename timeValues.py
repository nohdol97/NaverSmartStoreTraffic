import random

def getWaitThreadTime():
    return random.uniform(30, 120)

def getWaitLoadingTime():
    return random.uniform(3, 5)

def getWaitScrollTime():
    return random.uniform(1, 2)

def getWaitInTargetWithDetailTime():
    return random.uniform(5, 10)

def getWaitInTargetTime():
    return random.uniform(5, 10)

def getWaitImageProductLoadingTime():
    return random.uniform(5, 10)

def getWaitRepeatingTime():
    return random.uniform(30, 60)