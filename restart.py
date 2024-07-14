from concurrent.futures import ThreadPoolExecutor
import time
from datetime import datetime, timedelta

import task
import timeValues
import cacheMaker
import requestData
import setValues

def makeCache():
    with ThreadPoolExecutor(max_workers=setValues.windowCount) as executor:
        futures = []
        for i in range(0, setValues.windowCount):
            futures.append(executor.submit(cacheMaker.create_cache, i))
            time.sleep(timeValues.getWaitStartThreadTime()) # 시간 간격으로 스레드 실행

def main(startTime):
    with ThreadPoolExecutor(max_workers=setValues.windowCount) as executor:
        futures = []
        for i in range(0, setValues.windowCount):
            futures.append(executor.submit(task.start, i, startTime))
            time.sleep(timeValues.getWaitStartThreadTime()) # 시간 간격으로 스레드 실행

def work(windowCount, maxPages, maxAttempts, targetCount, unit, searchOption):
    # 전달된 인자 처리
    setValues.windowCount = windowCount
    setValues.maxPages = maxPages
    setValues.maxAttempts = maxAttempts
    setValues.targetCount = targetCount
    setValues.unit = unit
    setValues.searchOption = searchOption

    while True:
        makeCache()
        startTime = datetime.now()
        main(startTime)
        now = datetime.now()
        print(f"finish time: {now}")
        next_day = startTime.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        if now < next_day:
            wait_time = (next_day - now).total_seconds()
            time.sleep(wait_time)
        else:
            time.sleep(300)
        requestData.get_product()
        requestData.get_ip()