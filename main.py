from concurrent.futures import ThreadPoolExecutor
import time

import task, timeValues

threadNum = 3
startNum = threadNum * 0

def main():
    with ThreadPoolExecutor(max_workers=threadNum) as executor:
        futures = []
        for i in range(startNum, startNum + threadNum):
            futures.append(executor.submit(task.start, i))
            time.sleep(timeValues.getWaitStartThreadTime()) # 시간 간격으로 스레드 실행

if __name__ == "__main__":
    main()