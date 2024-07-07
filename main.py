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
        print("Executing get_product...")
        requestData.get_product()
    except Exception as e:
        print(f"Exception in get_product: {e}")

    try:
        print("Executing get_ip...")
        requestData.get_ip()
    except Exception as e:
        print(f"Exception in get_ip: {e}")

    print("Scheduled tasks executed at 23:45")

def check_end_time(executor, stop_event):
    while not stop_event.is_set():
        now = datetime.now()
        end_time = now.replace(hour=23, minute=45, second=0, microsecond=0)

        if now >= end_time:
            # 종료 시간 도달, 모든 작업을 종료
            print("종료 시간 도달, 모든 작업을 종료합니다.")
            stop_event.set()  # 작업 종료 신호 설정
            executor.shutdown(wait=True)
            execute_scheduled_tasks()

            # 00:00까지 대기
            next_start_time = now + timedelta(days=1)
            next_start_time = next_start_time.replace(hour=0, minute=0, second=0, microsecond=0)
            while datetime.now() < next_start_time:
                time.sleep(10)

            # 작업 재개
            print("작업 재개 시간 도달, 모든 작업을 재개합니다.")
            stop_event.clear()  # 작업 재개 신호 설정 해제
            return  # 함수 종료로 main() 함수 재호출을 방지

        time.sleep(10)

def main():
    stop_event = threading.Event()
    with ThreadPoolExecutor(max_workers=threadNum) as executor:
        futures = []
        end_time_thread = threading.Thread(target=check_end_time, args=(executor, stop_event))
        end_time_thread.start()

        for i in range(startNum, startNum + threadNum):
            futures.append(executor.submit(task.start, i))
            time.sleep(timeValues.getWaitStartThreadTime())  # 시간 간격으로 스레드 실행

        for future in futures:
            try:
                future.result()  # 작업이 완료될 때까지 대기
            except Exception as e:
                print(f"Exception in task: {e}")

if __name__ == "__main__":
    while True:
        main()
        # 다음 실행 시간을 계산
        now = datetime.now()
        next_start_time = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        sleep_duration = (next_start_time - now).total_seconds()
        print(f"Sleeping for {sleep_duration} seconds until next cycle.")
        time.sleep(sleep_duration)