import random
import setValues

def getWaitStartThreadTime():
    return random.uniform(10, 15)

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
    return random.uniform(3, 5)

def getWaitLoadingTimeForCache():
    return random.uniform(3, 5)

def getWakeWaitingTime():
    return random.uniform(10, 100)

def getAddMoreTime(): # 기본 체류 시간 30초
    return random.randint(0, max(0, setValues.maxTime - 30))