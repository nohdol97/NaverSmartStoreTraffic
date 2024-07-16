from concurrent.futures import ProcessPoolExecutor
import time
from datetime import datetime, timedelta

import task
import timeValues
import cacheMaker
import requestData
import setValues

def make_cache():
    with ProcessPoolExecutor(max_workers=setValues.windowCount) as executor:
        futures = []
        for i in range(setValues.windowCount):
            futures.append(executor.submit(cacheMaker.create_cache, i))
            time.sleep(timeValues.getWaitStartThreadTime())

def main(startTime):
    with ProcessPoolExecutor(max_workers=setValues.windowCount) as executor:
        futures = []
        for i in range(setValues.windowCount):
            futures.append(executor.submit(task.start, i, startTime))
            time.sleep(timeValues.getWaitStartThreadTime())

def work(windowCount, maxPages, maxAttempts, targetCount, unit, maxTime, searchOption):
    setValues.windowCount = windowCount
    setValues.maxPages = maxPages
    setValues.maxAttempts = maxAttempts
    setValues.targetCount = targetCount
    setValues.unit = unit
    setValues.maxTime = maxTime
    setValues.searchOption = searchOption

    while True:
        if check_product_list():
            make_cache()
        startTime = datetime.now()
        if check_product_list():
            main(startTime)
        now = datetime.now()
        print(f"finish time: {now}")
        next_day = startTime.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        if now < next_day:
            wait_time = (next_day - now).total_seconds()
            time.sleep(wait_time)
        else:
            time.sleep(300)
        time.sleep(timeValues.getWakeWaitingTime())
        requestData.get_product()
        time.sleep(3)
        requestData.get_ip()
        time.sleep(3)

def check_product_list():
    try:
        with open('product_list.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip().replace(' ', '') for line in file if line.strip()]
        
        if not lines:
            return False
        
        for line in lines:
            if not line:  # 줄이 띄어쓰기만 있는 경우
                return False
        
        print("작업을 시작합니다.")
        return True
    except:
        print("product_list.txt 가 없습니다.")
        return False