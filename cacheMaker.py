from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os, random, shutil, time

import chromeOptions
import util.findUtil as findUtil
import util.loginUtil as loginUtil
import util.accessShoppingUtil as accessShoppingUtil
import productList, timeValues, driverInfo
import setValues

def create_cache(cache_number):
    profile_dir = os.path.join(os.getcwd(), f"chrome_profile{cache_number}")

    # 프로필 디렉토리 생성
    if os.path.exists(profile_dir):
        shutil.rmtree(profile_dir)
        os.makedirs(profile_dir)
    else:
        os.makedirs(profile_dir)

    # Chrome option 설정
    chrome_options = webdriver.ChromeOptions()
    # chromeOptions.addMobile(chrome_options) 절대 하면 안됨
    chromeOptions.addOptimization(chrome_options, profile_dir)

    # Xvfb 설정
    os.environ['DISPLAY'] = ':99'

    # ChromeDriver를 webdriver_manager를 사용하여 자동으로 설치 및 설정
    service = Service(ChromeDriverManager().install())
    # 랜덤한 개수의 랜덤한 URL 선택
    with open('cacheUrls.txt', 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file if line.strip()]  # 빈 줄을 무시
    random.shuffle(urls)
    num_urls = random.randint(7, 15) # 랜덤한 개수 선택
    selected_urls = random.sample(urls, num_urls)  # 랜덤한 URL들을 선택
    for url in selected_urls:
        try:
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.set_page_load_timeout(timeValues.getWaitLoadingTimeForCache())  # 페이지 로딩 타임아웃 설정 (초)
            driver.get(url)
            time.sleep(2)
            driverInfo.kill_driver(driver, None)
        except Exception as e:
            driverInfo.kill_driver(driver, None)

    driverInfo.kill_driver(driver, None)

    # # 네이버 상품용 캐시
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    # try:
    #     driver.set_page_load_timeout(60)  # 페이지 로딩 타임아웃 설정 (초)
    #     for midValueKeywordStr in productList.getMidValueKeywordList():
    #         product = midValueKeywordStr.split(',')
    #         if (len(product) == 6):
    #             mid_value, comparison_mid_value, keyword = product[2], product[3], product[4]
    #             if setValues.searchOption == "통검":
    #                 access = accessShoppingUtil.access_total_random(driver, keyword)
    #                 find, page, ranking = findUtil.findTargetByMidValue(driver, comparison_mid_value, keyword, False, False)
    #             elif setValues.searchOption == "쇼검":
    #                 # access = accessShoppingUtil.access_by_shopping(driver, keyword)
    #                 access = accessShoppingUtil.access_total_random(driver, keyword)
    #                 find, page, ranking = findUtil.findTargetByMidValue(driver, comparison_mid_value, keyword, False, False)
    #             elif setValues.searchOption == "통검&쇼검":
    #                 access = accessShoppingUtil.access_total_random(driver, keyword)
    #                 find, page, ranking = findUtil.findTargetByMidValue(driver, comparison_mid_value, keyword, False, False)
    #                 # access = accessShoppingUtil.access_by_shopping(driver, keyword)
    #                 # find, page, ranking = findUtil.findTargetByMidValue(driver, comparison_mid_value, keyword, False, False)
    #             if not access:
    #                 break
    #         else:
    #             mid_value, keyword = product[2], product[3]
    #             if setValues.searchOption == "통검":
    #                 access = accessShoppingUtil.access_total_random(driver, keyword)
    #                 find, page, ranking = findUtil.findTargetByMidValue(driver, mid_value, keyword, False, False)
    #             elif setValues.searchOption == "쇼검":
    #                 # access = accessShoppingUtil.access_by_shopping(driver, keyword)
    #                 access = accessShoppingUtil.access_total_random(driver, keyword)
    #                 find, page, ranking = findUtil.findTargetByMidValue(driver, mid_value, keyword, False, False)
    #             elif setValues.searchOption == "통검&쇼검":
    #                 access = accessShoppingUtil.access_total_random(driver, keyword)
    #                 find, page, ranking = findUtil.findTargetByMidValue(driver, mid_value, keyword, False, False)
    #                 # access = accessShoppingUtil.access_by_shopping(driver, keyword)
    #                 # find, page, ranking = findUtil.findTargetByMidValue(driver, mid_value, keyword, False, False)
    #             if not access:
    #                 break
    #         # if not find:
    #         #     productList.errorProduct(mid_value)
    # except:
    #     pass

    # # 드라이버 종료
    # driverInfo.kill_driver(driver, None)