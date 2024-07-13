from concurrent.futures import ThreadPoolExecutor
import time
from datetime import datetime, timedelta

import task
import timeValues
import cacheMaker
import requestData
import setValues

def makeCache(startNum, endNum):
    with ThreadPoolExecutor(max_workers=endNum-startNum) as executor:
        futures = []
        for i in range(startNum, endNum):
            futures.append(executor.submit(cacheMaker.create_cache, i))
            time.sleep(timeValues.getWaitStartThreadTime()) # 시간 간격으로 스레드 실행

def main(startTime):
    with ThreadPoolExecutor(max_workers=setValues.threadNum) as executor:
        futures = []
        for i in range(0, setValues.threadNum):
            futures.append(executor.submit(task.start, i, startTime))
            time.sleep(timeValues.getWaitStartThreadTime()) # 시간 간격으로 스레드 실행

if __name__ == "__main__":
    while True:
        # startNum = setValues.threadNum // 2
        # makeCache(0, startNum)
        # time.sleep(10)
        # makeCache(startNum, setValues.threadNum)
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
        makeCache(0, setValues.threadNum)