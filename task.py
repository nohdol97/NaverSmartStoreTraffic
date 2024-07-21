import time, random
import shutil
import work, setValues
import timeValues as timeValues
import traceback
import productList
import driverInfo
import util.loginUtil as loginUtil
import util.accessShoppingUtil as accessShoppingUtil
import hiPaiProxy
from datetime import datetime

def process_product(driver, proxy, mid_value, comparison_mid_value, keyword, is_comparison=False):
    if is_comparison:
        result = work.mobilePriceComparisonNaverShopping(driver, mid_value, comparison_mid_value, keyword)
    else:
        result = work.mobileNaverShopping(driver, mid_value, keyword)
    
    if result:
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

def handle_product(driver, proxy, product):
    product_parts = product.split(',')
    if len(product_parts) == 6:  # 원부 검색
        mid_value, comparison_mid_value, keyword = product_parts[2], product_parts[3], product_parts[4]
        # 로그인 필요하면 여기에 추가
        # loginUtil.login_with_account(driver, id, pw)
        # access = accessShoppingUtil.access_direct(driver, keyword)
        access = accessShoppingUtil.access_total_random(driver, keyword)
        if access:
            return process_product(driver, proxy, mid_value, comparison_mid_value, keyword, is_comparison=True)
    else:
        mid_value, keyword = product_parts[2], product_parts[3]
        # access = accessShoppingUtil.access_direct(driver, keyword)
        access = accessShoppingUtil.access_total_random(driver, keyword)
        if access:
            return process_product(driver, proxy, mid_value, None, keyword, is_comparison=False)
    return False

def start(profileNum, startTime):
    while True:
        if productList.checkFinish(startTime):
            driverInfo.kill_driver(driver, None)
            break
        try:
            driver, temp_profile_dir, proxy = driverInfo.make_driver(profileNum)
            driver.set_page_load_timeout(50)  # 페이지 로딩 타임아웃 설정 (초)
            total, products = productList.getMidValueKeywordList()
            for midValueKeywordStr in products:
                try:
                    if not productList.checkProductNum(midValueKeywordStr):
                        continue
                    result = handle_product(driver, proxy, midValueKeywordStr)
                    if not result:
                        break
                except Exception as e:
                    print(f"Error: {e}")
                    traceback.print_exc()
                time.sleep(timeValues.getWaitLoadingTime())
            
            driverInfo.kill_driver(driver, proxy)
        except:
            driverInfo.kill_driver(driver, proxy)

        # 임시 프로필 디렉토리 삭제
        for i in range(10):
            try:
                shutil.rmtree(temp_profile_dir)
                break
            except:
                time.sleep(3)

        if result:
            current_time = datetime.now()
            workDoneNum = len(products)
            sleep_time = get_sleep_time(current_time, workDoneNum, total)
            time.sleep(sleep_time) # 일정시간 대기
        else:
            time.sleep(timeValues.getWaitRepeatingTime())

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