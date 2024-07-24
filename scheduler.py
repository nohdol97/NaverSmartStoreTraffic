import schedule
import time, os
from threading import Thread, Event
from datetime import datetime
import requestData

def run_scheduler(stop_event):
    while not stop_event.is_set():
        now = datetime.now()
        # id 가져오기
        check_and_get_id(10, 23, 0)
        check_and_get_id(14, 23, 0)
        check_and_get_id(18, 23, 0)

        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    stop_event = Event()
    scheduler_thread = Thread(target=run_scheduler, args=(stop_event,))
    scheduler_thread.start()
    return stop_event, scheduler_thread

def check_and_get_id(hour, minute, second):
    now = datetime.now()
    if now.hour == hour and now.minute == minute and now.second == second:
        try:
            # 아이디 존재 확인, 없다면 요청
            file_path = 'id.txt'
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    content = file.read()
                    if not content:
                        requestData.get_id()
            else:
                requestData.get_id()
        except Exception as e:
            print(f"Exception in check_and_get_id: {e}")
        time.sleep(1)  # 1초 대기하여 중복 실행 방지