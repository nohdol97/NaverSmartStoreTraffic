from concurrent.futures import ThreadPoolExecutor
import time

import task, values, timeValues

startNum = values.threadNum * 1

def main2():
    with ThreadPoolExecutor(max_workers=values.threadNum) as executor:
        futures = []
        for i in range(startNum, startNum + values.threadNum):
            futures.append(executor.submit(task.start, i))
            time.sleep(timeValues.getWaitThreadTime()) # 시간 간격으로 스레드 실행

if __name__ == "__main1__":
    main2()