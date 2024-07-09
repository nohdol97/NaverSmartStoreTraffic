from concurrent.futures import ThreadPoolExecutor
import time
import threading
from datetime import datetime, timedelta

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

def schedule_daily_task(execute_time, task_function):
    def scheduler():
        while True:
            now = datetime.now()
            next_run = now.replace(hour=execute_time.hour, minute=execute_time.minute, second=0, microsecond=0)
            if now >= next_run:
                next_run += timedelta(days=1)
            sleep_time = (next_run - now).total_seconds()
            time.sleep(sleep_time)
            task_function()

    threading.Thread(target=scheduler, daemon=True).start()

def main():
    with ThreadPoolExecutor(max_workers=threadNum) as executor:
        futures = []
        for i in range(startNum, startNum + threadNum):
            futures.append(executor.submit(task.start, i))
            time.sleep(timeValues.getWaitThreadTime()) # 시간 간격으로 스레드 실행

    # Schedule the daily task
    execute_time = datetime.strptime("23:55", "%H:%M").time()
    schedule_daily_task(execute_time, execute_scheduled_tasks)

if __name__ == "__main__":
    main()