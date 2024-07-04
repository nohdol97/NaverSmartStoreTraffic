import time, shutil
import work
import timeValues as timeValues
import traceback
import productList
import driverInfo
import util.loginUtil as loginUtil
import hiPaiProxy

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

threadNum = 10

def task(profileNum):
    while True:
        if productList.checkFinish():
            print(f"finish time: {datetime.now()}")
            break

        driver, temp_profile_dir, proxy = driverInfo.create_driver(profileNum)

        for midValueKeywordStr in productList.getMidValueKeywordList():
            try:
                if not productList.checkProductNum(midValueKeywordStr):
                    continue
                loginUtil.naverHome(driver)
                # ip 바꾸면서 5번 시도
                for j in range(5):
                    mid_value, keyword = midValueKeywordStr.split(',')[:2]
                    result = work.mobileNaverShopping(driver, mid_value, keyword)
                    if result:
                        productList.decreaseNum(mid_value)
                        break
                    else:
                        # 실패했으면 제거한 proxy를 파일의 마지막에 다시 추가
                        hiPaiProxy.addProxyIp(proxy)

                        driver.quit()
                        time.sleep(timeValues.getWaitLoadingTime())
                        driver, temp_profile_dir, proxy = driverInfo.create_driver(profileNum)
                        loginUtil.naverHome(driver)

                # url ="https://search.naver.com/search.naver?ssc=tab.image.all&where=image&query=%22%ED%8B%B0%EB%B9%84+%EC%8A%A4%ED%83%A0%EB%93%9C+%EC%82%BC%ED%83%A0%EB%B0%94%EC%9D%B4%EB%AF%B8+%EC%9D%B4%EB%8F%99%EC%8B%9D+%EA%B1%B0%EC%B9%98%EB%8C%80+LG+%EC%82%BC%EC%84%B1+%EC%A4%91%EC%86%8C+%EB%B2%A0%EC%82%AC%ED%99%80+100%ED%98%B8%ED%99%98%22&sm=tab_dgs&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall#imgId=image_sas%3Anshopping_fd30779427f7287b35484c52e5d84bea"
                # work.mobileNaverImageShopping(driver, url)
            except Exception as e:
                print(f"Error: {e}")
                traceback.print_exc()
            time.sleep(timeValues.getWaitLoadingTime())
        driver.quit()

        # 끝났으면 사용한 proxy를 파일의 마지막에 다시 추가
        hiPaiProxy.addProxyIp(proxy)

        # 임시 프로필 디렉토리 삭제
        shutil.rmtree(temp_profile_dir)
        time.sleep(timeValues.getWaitRepeatingTime()) # 일정시간 대기

def main():
    with ThreadPoolExecutor(max_workers=threadNum) as executor:
        futures = []
        for i in range(threadNum):
            futures.append(executor.submit(task, i))
            time.sleep(timeValues.getWaitThreadTime()) # 시간 간격으로 스레드 실행

if __name__ == "__main__":
    main()