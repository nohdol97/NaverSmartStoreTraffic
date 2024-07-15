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
        requestData.get_product()
        time.sleep(3)
        requestData.get_ip()
        time.sleep(3)
        if check_product_list():
            makeCache()
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

def check_product_list():
    try:
        with open('product_list.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip().replace(' ', '') for line in file if line.strip()]
        
        if not lines:
            return False
        
        for line in lines:
            parts = line.split(',')
            if parts[-1] == '0':
                return False
        
        print("작업을 시작합니다.")
        return True
    except:
        print("product_list.txt 가 없습니다.")
        return False