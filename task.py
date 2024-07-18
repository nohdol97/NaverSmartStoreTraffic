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
        access = accessShoppingUtil.access_direct(driver, keyword)
        if access:
            return process_product(driver, proxy, mid_value, comparison_mid_value, keyword, is_comparison=True)
    else:
        mid_value, keyword = product_parts[2], product_parts[3]
        access = accessShoppingUtil.access_direct(driver, keyword)
        if access:
            return process_product(driver, proxy, mid_value, None, keyword, is_comparison=False)
    return False

def start(profileNum, startTime):
    while True:
        if productList.checkFinish(startTime):
            break
        success = False
        try:
            driver, temp_profile_dir, proxy = driverInfo.make_driver(profileNum)
            driver.set_page_load_timeout(50)  # 페이지 로딩 타임아웃 설정 (초)
            current_time = datetime.now()
            products = productList.getMidValueKeywordList()
            for midValueKeywordStr in products:
                try:
                    if not productList.checkProductNum(midValueKeywordStr):
                        continue
                    
                    if not handle_product(driver, proxy, midValueKeywordStr):
                        break
                except Exception as e:
                    print(f"Error: {e}")
                    traceback.print_exc()
                time.sleep(timeValues.getWaitLoadingTime())
            
            driverInfo.kill_driver(driver, proxy)
            success = True
        except:
            driverInfo.kill_driver(driver, proxy)

        # 임시 프로필 디렉토리 삭제
        for i in range(10):
            try:
                shutil.rmtree(temp_profile_dir)
                break
            except:
                time.sleep(3)

        workDoneNum = len(products)
        if 0 <= current_time.hour < 7:
            sleep_time = random.uniform(*setValues.waitTimes["0~7시"]) * workDoneNum * setValues.windowCount
        elif 7 <= current_time.hour < 10:
            sleep_time = random.uniform(*setValues.waitTimes["7~10시"]) * workDoneNum * setValues.windowCount
        elif 10 <= current_time.hour < 14:
            sleep_time = random.uniform(*setValues.waitTimes["10~14시"]) * workDoneNum * setValues.windowCount
        elif 14 <= current_time.hour < 17:
            sleep_time = random.uniform(*setValues.waitTimes["14~17시"]) * workDoneNum * setValues.windowCount
        else:
            sleep_time = random.uniform(*setValues.waitTimes["17시 이후"]) * workDoneNum * setValues.windowCount
        if success:
            time.sleep(sleep_time) # 일정시간 대기
        else:
            time.sleep(timeValues.getWaitRepeatingTime())