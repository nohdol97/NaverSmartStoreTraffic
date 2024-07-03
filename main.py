import time, shutil, random
import work
import timeValues as timeValues
import traceback
import productList
import driverInfo
import util.loginUtil as loginUtil
import util.randomUtil as randomUtil
import hiPaiProxy

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

threadNum = 10

def task(profileNum):
    while True:
        if productList.checkFinish():
            print(f"finish time: {datetime.now()}")
            break
        # with open('accounts.txt', 'r') as file:
        #     lines = file.readlines()

        # # 각 줄에서 ','로 분할한 부분이 2개인 줄만 필터링
        # filtered_lines = [line for line in lines if len(line.split(',')) == 2]

        # # filtered_lines가 비어있지 않다면 랜덤하게 한 줄 선택
        # randomValue = randomUtil.get_random_value()
        # if randomValue < 0.6: # 60퍼 확률
        #     if filtered_lines:
        #         random_line = random.choice(filtered_lines)

        #         line = random_line.strip()
        #         naverid, naverpassword = line.split(',')

        #         driver, temp_profile_dir, isLogin = driverInfo.create_driver(profileNum, naverid)
        #         if isLogin:
        #             # 로그인
        #             try:
        #                 loginUtil.login_with_account(driver, naverid, naverpassword)
        #                 # accounts.txt 에서 line 에 해당하는 줄 가장 뒤에 ',used' 를 추가
        #                 loginUtil.update_account_status(random_line)
        #             except:
        #                 pass
        #         else:
        #             loginUtil.naverHome(driver) 
        #     else:
        #         driver, temp_profile_dir, isLogin = driverInfo.create_driver(profileNum)
        #         loginUtil.naverHome(driver)
        # else:
        #     driver, temp_profile_dir, isLogin = driverInfo.create_driver(profileNum)
        #     loginUtil.naverHome(driver)

        driver, temp_profile_dir, proxy = driverInfo.create_driver(profileNum)

        for midValueKeywordStr in productList.getMidValueKeywordList():
            try:
                if not productList.checkNegative(midValueKeywordStr):
                    continue
                loginUtil.naverHome(driver)
                for j in range(5):
                    result = work.mobileNaverShopping(driver, midValueKeywordStr)
                    if result:
                        break
                    else:
                        # 실패했으면 제거한 proxy를 파일의 마지막에 다시 추가
                        hiPaiProxy.setProxyIp(proxy)

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

        if result:
            hiPaiProxy.setProxyIp(proxy)
            productList.decreaseNum()

        # # hiPaiProxy.txt 내에 아이디 지움
        # hiPaiProxy.eraseID(naverid)

        # 임시 프로필 디렉토리 삭제
        shutil.rmtree(temp_profile_dir)
        time.sleep(random.randint(200, 300)) # 일정시간 대기

def main():
    with ThreadPoolExecutor(max_workers=threadNum) as executor:
        futures = []
        for i in range(threadNum):
            futures.append(executor.submit(task, i))
            time.sleep(random.randint(60, 120)) # 시간 간격으로 스레드 실행

if __name__ == "__main__":
    main()