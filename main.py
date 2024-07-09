from concurrent.futures import ThreadPoolExecutor
import time
import schedule
from threading import Thread

import task
import timeValues
import requestData

# 쓰레드 풀 설정
threadNum = 3
startNum = threadNum * 0

def execute_scheduled_tasks():
    try:
        requestData.get_product()
    except Exception as e:
        print(f"Exception in get_product: {e}")

    try:
        requestData.get_ip()
    except Exception as e:
        print(f"Exception in get_ip: {e}")

    print("Scheduled tasks executed at 23:55")

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    schedule.every().day.at("23:55").do(execute_scheduled_tasks)
    
    scheduler_thread = Thread(target=run_scheduler)
    scheduler_thread.start()

def main():
    with ThreadPoolExecutor(max_workers=threadNum) as executor:
        futures = []
        for i in range(startNum, startNum + threadNum):
            futures.append(executor.submit(task.start, i))
            time.sleep(timeValues.getWaitStartThreadTime()) # 시간 간격으로 스레드 실행

if __name__ == "__main__":
    start_scheduler()
    main()