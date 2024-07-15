import time
import shutil
import work
import timeValues as timeValues
import traceback
import productList
import driverInfo
import util.loginUtil as loginUtil
import util.accessShoppingUtil as accessShoppingUtil
import hiPaiProxy

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
    if len(product_parts) == 4:  # 원부 검색
        mid_value, comparison_mid_value, keyword = product_parts[0], product_parts[1], product_parts[2]
        # 로그인 필요하면 여기에 추가
        # loginUtil.login_with_account(driver, id, pw)
        access = accessShoppingUtil.access_direct(driver, keyword)
        if access:
            return process_product(driver, proxy, mid_value, comparison_mid_value, keyword, is_comparison=True)
    else:
        mid_value, keyword = product_parts[0], product_parts[1]
        access = accessShoppingUtil.access_direct(driver, keyword)
        if access:
            return process_product(driver, proxy, mid_value, None, keyword, is_comparison=False)
    return False

def start(profileNum, startTime):
    while True:
        if productList.checkFinish(startTime):
            break
        
        driver, temp_profile_dir, proxy = driverInfo.make_driver(profileNum)

        for midValueKeywordStr in productList.getMidValueKeywordList():
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

        # 임시 프로필 디렉토리 삭제
        for i in range(10):
            try:
                shutil.rmtree(temp_profile_dir)
                break
            except:
                time.sleep(3)
        time.sleep(timeValues.getWaitRepeatingTime()) # 일정시간 대기