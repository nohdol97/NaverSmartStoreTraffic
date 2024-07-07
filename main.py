from concurrent.futures import ThreadPoolExecutor
import time
import threading
from datetime import datetime, timedelta, timezone

import task
import timeValues
import requestData

# 쓰레드 풀 설정
threadNum = 3
startNum = threadNum * 0

# 한국 시간대 설정
KST = timezone(timedelta(hours=9))

def execute_scheduled_tasks():
    # 23:30에 get_product()와 get_ip()를 호출
    requestData.get_product()
    requestData.get_ip()
    print("Scheduled tasks executed at 23:30")

def check_end_time(executor):
    while True:
        now = datetime.now(KST)
        end_time = now.replace(hour=23, minute=30, second=0, microsecond=0)

        if now >= end_time:
            # 종료 시간 도달, 모든 작업을 종료
            print("종료 시간 도달, 모든 작업을 종료합니다.")
            executor.shutdown(wait=False)
            execute_scheduled_tasks()

            # 00:00까지 대기
            next_start_time = now.replace(day=now.day + 1, hour=0, minute=0, second=0, microsecond=0)
            while datetime.now(KST) < next_start_time:
                time.sleep(10)
            
            # 작업 재개
            print("작업 재개 시간 도달, 모든 작업을 재개합니다.")
            main()
            break
        
        time.sleep(10)

def main():
    with ThreadPoolExecutor(max_workers=threadNum) as executor:
        futures = []
        end_time_thread = threading.Thread(target=check_end_time, args=(executor,))
        end_time_thread.start()
        
        for i in range(startNum, startNum + threadNum):
            futures.append(executor.submit(task.start, i))
            time.sleep(timeValues.getWaitStartThreadTime())  # 시간 간격으로 스레드 실행

if __name__ == "__main__":
    main()