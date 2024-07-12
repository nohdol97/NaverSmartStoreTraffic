import time, shutil
import work
import timeValues as timeValues
import traceback
import productList
import driverInfo
import util.loginUtil as loginUtil
import util.accessShoppingUtil as accessShoppingUtil
import hiPaiProxy

def start(profileNum, startTime):
    while True:
        if productList.checkFinish(startTime):
            break
        
        driver, temp_profile_dir, proxy = driverInfo.make_driver(profileNum)

        for midValueKeywordStr in productList.getMidValueKeywordList():
            try:
                if not productList.checkProductNum(midValueKeywordStr):
                    continue

                # 상품 찾기 시도
                product = midValueKeywordStr.split(',')
                if (len(product) == 4): # 원부 검색
                    mid_value, comparison_mid_value, keyword = product[0], product[1], product[2]
                    # 로그인 필요하면 여기에 추가
                    # loginUtil.login_with_account(driver, id, pw)
                    access = accessShoppingUtil.access_direct(driver, keyword)
                    if access:
                        result = work.mobilePriceComparisonNaverShopping(driver, mid_value, comparison_mid_value, keyword)
                        if result:
                            productList.decreaseNum(mid_value)
                    else:
                        break
                else:
                    mid_value, keyword = product[0], product[1]
                    # 로그인 필요하면 여기에 추가
                    # loginUtil.login_with_account(driver, id, pw)
                    access = accessShoppingUtil.access_direct(driver, keyword)
                    if access:
                        # 내부에서 tryFinding 으로 maxFind번 시도중
                        result = work.mobileNaverShopping(driver, mid_value, keyword)
                        if result:
                            productList.decreaseNum(mid_value)
                        else:
                            # 실패했으면 제거한 proxy를 파일의 마지막에 다시 추가
                            hiPaiProxy.addProxyIp(proxy)
                            # productList.errorProduct(mid_value)
                    else:
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