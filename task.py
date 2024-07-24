import time as t
import random, os
import shutil
import work, setValues
import timeValues as timeValues
import traceback
import productList
import driverInfo
import util.loginUtil as loginUtil
import util.accessShoppingUtil as accessShoppingUtil
import hiPaiProxy
from datetime import datetime, time

def process_product(driver, proxy, mid_value, comparison_mid_value, keyword, is_comparison, id):
    if is_comparison:
        result = work.mobilePriceComparisonNaverShopping(driver, mid_value, comparison_mid_value, keyword)
    else:
        result = work.mobileNaverShopping(driver, mid_value, keyword)
    
    if id and result:
        print(f'access success id: {id}, keyword: {keyword}')
    elif result:
        productList.decreaseNum(mid_value)
        print_product_list()
    else:
        hiPaiProxy.addProxyIp(proxy)
    
    return result

def print_product_list():
    for i in range(10):
        try:
            with open('product_list.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
            for line in lines:
                print(line.strip())
            print()  # 마지막에 엔터 하나 추가
            break
        except:
            pass

def handle_product(driver, proxy, product, id = None, pw = None):
    product_parts = product.split(',')
    
    if id:
        if len(product_parts) == 3:  # 원부 검색
            mid_value, comparison_mid_value, keyword = product_parts[0], product_parts[1], product_parts[2]
            # access = accessShoppingUtil.access_direct(driver, keyword)
            access = accessShoppingUtil.access_total_random(driver, keyword)
            if access:
                return process_product(driver, proxy, mid_value, comparison_mid_value, keyword, True, id)
        else:
            mid_value, keyword = product_parts[0], product_parts[1]
            # access = accessShoppingUtil.access_direct(driver, keyword)
            access = accessShoppingUtil.access_total_random(driver, keyword)
            if access:
                return process_product(driver, proxy, mid_value, None, keyword, False, id)
        append_to_file('id.txt', id, pw)
    else:
        if len(product_parts) == 6:  # 원부 검색
            mid_value, comparison_mid_value, keyword = product_parts[2], product_parts[3], product_parts[4]
            # 로그인 필요하면 여기에 추가
            # loginUtil.login_with_account(driver, id, pw)
            # access = accessShoppingUtil.access_direct(driver, keyword)
            access = accessShoppingUtil.access_total_random(driver, keyword)
            if access:
                return process_product(driver, proxy, mid_value, comparison_mid_value, keyword, True, id)
        else:
            mid_value, keyword = product_parts[2], product_parts[3]
            # access = accessShoppingUtil.access_direct(driver, keyword)
            access = accessShoppingUtil.access_total_random(driver, keyword)
            if access:
                return process_product(driver, proxy, mid_value, None, keyword, False, id)
    return False

def start(profileNum, startTime):
    id, pw = None, None
    while True:
        try:
            now = datetime.now().time()
            if setValues.searchOption == "ID" and is_within_time_ranges(now, time_ranges):
                while True:
                    file_path = 'id.txt'
                    if os.path.exists(file_path):
                        with open(file_path, 'r') as file:
                            content = file.read()
                            if not content:
                                t.sleep(300)
                            else:
                                break
                    else:
                        t.sleep(300)

            driver, temp_profile_dir, proxy = driverInfo.make_driver(profileNum)
            driver.set_page_load_timeout(50)  # 페이지 로딩 타임아웃 설정 (초)

            if not id:
                if setValues.searchOption == "ID":
                    id, pw = read_first_line_and_update_file('id.txt')
            
            if id:
                with open('product_for_id.txt', 'r', encoding='utf-8') as file:
                    products = [line.strip() for line in file if line.strip()]  # 빈 줄을 무시
            else:
                total, products = productList.getMidValueKeywordList()

            if id:
                loginUtil.login_with_account(driver, id, pw)

            for midValueKeywordStr in products:
                try:
                    if productList.checkFinish(startTime, id):
                        driverInfo.kill_driver(driver, None)
                        break
                    if not id:
                        if not productList.checkProductNum(midValueKeywordStr):
                            continue
                    result = handle_product(driver, proxy, midValueKeywordStr, id, pw)
                    if not result:
                        break
                except Exception as e:
                    print(f"Error: {e}")
                    traceback.print_exc()
                t.sleep(timeValues.getWaitLoadingTime())
            
            driverInfo.kill_driver(driver, proxy)
        except:
            driverInfo.kill_driver(driver, proxy)

        # 임시 프로필 디렉토리 삭제
        for i in range(10):
            try:
                shutil.rmtree(temp_profile_dir)
                break
            except:
                t.sleep(3)
        
        if productList.checkFinish(startTime, id):
            driverInfo.kill_driver(driver, None)
            break
        
        if id and result:
            id = None
            pw = None
            t.sleep(timeValues.getWaitRepeatingTime())
        elif result:
            current_time = datetime.now()
            workDoneNum = len(products)
            sleep_time = get_sleep_time(current_time, workDoneNum, total)
            t.sleep(sleep_time) # 일정시간 대기
        else:
            t.sleep(timeValues.getWaitRepeatingTime())

def get_sleep_time(current_time, workDoneNum, total):
    for time_range in setValues.waitTimes.keys():
        if time_range == "그 외":
            continue  # "그 외"는 마지막에 처리

        start_hour, end_hour = map(int, time_range.replace("시", "").split("~"))
        
        if start_hour <= current_time.hour < end_hour:
            sleep_time = random.uniform(*setValues.waitTimes[time_range]) * workDoneNum * (setValues.targetCount // int(total))
            print(f'sleep time : {sleep_time}')
            return sleep_time

    # "그 외" 범위를 기본값으로 사용
    sleep_time = random.uniform(*setValues.waitTimes["그 외"]) * workDoneNum * (setValues.targetCount // int(total))
    print(f'sleep time : {sleep_time}')
    return sleep_time

def read_first_line_and_update_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    if not lines:
        return None, None
    
    first_line = lines[0].strip()
    remaining_lines = lines[1:]
    
    with open(file_path, 'w') as file:
        file.writelines(remaining_lines)
    
    id, pw = first_line.split(',')
    return id, pw

def append_to_file(file_path, id, pw):
    with open(file_path, 'a') as file:
        file.write(f"{id},{pw}\n")

def is_within_time_ranges(now, time_ranges):
    for start_time, end_time in time_ranges:
        if start_time <= now <= end_time:
            return True
    return False

time_ranges = [
    (time(9, 30), time(10, 30)),    # 9:30 AM ~ 10:30 AM
    (time(13, 30), time(14, 30)),   # 1:30 PM ~ 2:30 PM
    (time(17, 30), time(18, 30))    # 5:30 PM ~ 6:30 PM
]