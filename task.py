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
        
        for i in range(10):
            try:
                driver, temp_profile_dir, proxy = driverInfo.create_driver(profileNum)
                break
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(3)

        for midValueKeywordStr in productList.getMidValueKeywordList():
            try:
                if not productList.checkProductNum(midValueKeywordStr):
                    continue
                # ip 바꾸면서 5번 시도
                for i in range(5):
                    product = midValueKeywordStr.split(',')
                    if (len(product) == 4):
                        mid_value, comparison_mid_value, keyword = product[0], product[1], product[2]
                        # 로그인 필요하면 여기에 추가
                        # loginUtil.login_with_account(driver, id, pw)
                        accessShoppingUtil.access_direct(driver, keyword)
                        result = work.mobilePriceComparisonNaverShopping(driver, mid_value, comparison_mid_value, keyword)
                    else:
                        mid_value, keyword = product[0], product[1]
                        # 로그인 필요하면 여기에 추가
                        # loginUtil.login_with_account(driver, id, pw)
                        accessShoppingUtil.access_direct(driver, keyword)
                        result = work.mobileNaverShopping(driver, mid_value, keyword)
                    if result:
                        productList.decreaseNum(mid_value)
                        break
                    else:
                        # 실패했으면 제거한 proxy를 파일의 마지막에 다시 추가
                        hiPaiProxy.addProxyIp(proxy)
                        driverInfo.kill_driver(driver)
                        time.sleep(timeValues.getWaitLoadingTime())
                        driver, temp_profile_dir, proxy = driverInfo.create_driver(profileNum)

                # url ="https://search.naver.com/search.naver?ssc=tab.image.all&where=image&query=%22%ED%8B%B0%EB%B9%84+%EC%8A%A4%ED%83%A0%EB%93%9C+%EC%82%BC%ED%83%A0%EB%B0%94%EC%9D%B4%EB%AF%B8+%EC%9D%B4%EB%8F%99%EC%8B%9D+%EA%B1%B0%EC%B9%98%EB%8C%80+LG+%EC%82%BC%EC%84%B1+%EC%A4%91%EC%86%8C+%EB%B2%A0%EC%82%AC%ED%99%80+100%ED%98%B8%ED%99%98%22&sm=tab_dgs&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall#imgId=image_sas%3Anshopping_fd30779427f7287b35484c52e5d84bea"
                # work.mobileNaverImageShopping(driver, url)
            except Exception as e:
                print(f"Error: {e}")
                # traceback.print_exc()
                driverInfo.kill_driver(driver)
            time.sleep(timeValues.getWaitLoadingTime())
        
        driverInfo.kill_driver(driver)

        # 끝났으면 사용한 proxy를 파일의 마지막에 다시 추가
        hiPaiProxy.addProxyIp(proxy)

        # 임시 프로필 디렉토리 삭제
        for i in range(10):
            try:
                shutil.rmtree(temp_profile_dir)
                break
            except:
                time.sleep(3)
        time.sleep(timeValues.getWaitRepeatingTime()) # 일정시간 대기