from concurrent.futures import ThreadPoolExecutor
import time
import schedule
from threading import Thread, Event
from datetime import datetime

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

def run_scheduler(stop_event):
    while not stop_event.is_set():
        now = datetime.now()
        # 23:55:00에 작업을 실행
        if now.hour == 23 and now.minute == 55 and now.second == 0:
            execute_scheduled_tasks()
            time.sleep(1)  # 1초 대기하여 중복 실행 방지
        schedule.run_pending()
        time.sleep(1)

def start_scheduler(stop_event):
    scheduler_thread = Thread(target=run_scheduler, args=(stop_event,))
    scheduler_thread.start()
    return scheduler_thread

def main():
    with ThreadPoolExecutor(max_workers=threadNum) as executor:
        futures = []
        for i in range(startNum, startNum + threadNum):
            futures.append(executor.submit(task.start, i))
            time.sleep(timeValues.getWaitStartThreadTime()) # 시간 간격으로 스레드 실행

if __name__ == "__main__":
    stop_event = Event()
    # 스케줄러 스레드를 시작합니다.
    scheduler_thread = start_scheduler(stop_event)
    
    # 메인 스레드에서 작업을 시작합니다.
    main()
    
    # 종료 시 스케줄러를 멈춥니다.
    stop_event.set()
    scheduler_thread.join()