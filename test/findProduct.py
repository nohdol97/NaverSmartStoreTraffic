import os, time, sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver
from selenium.common.exceptions import WebDriverException

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import util.findUtil as findUtil
import util.countUtil as countUtil
import util.clickUtil as clickUtil
import allElements
import chromeOptions

maxFind = 3
maxPage = 20

def findProductByMidValue():
    driver = createDriverTest()

    # 현재 디렉토리 경로
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 상위 디렉토리 경로
    parent_dir = os.path.dirname(current_dir)
    # 상위 디렉토리에 있는 파일 경로
    file_path = os.path.join(parent_dir, 'product_list.txt')
    # 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]

    # 각 줄 출력
    for line in lines[1:]:
        mid_value, keyword = line.split(',')[:2]
        print(f"midValue({mid_value}), keyword({keyword})")
        url = f"https://msearch.shopping.naver.com/search/all?query={keyword}"

        driver.get(url)
        time.sleep(3)

        page, ranking = findUtil.findTargetByMidValue(driver, mid_value, False)

        print(f"page({page}), ranking({ranking})")
        
def createDriverTest():
    # Chrome option 설정
    chrome_options = webdriver.ChromeOptions()
    chromeOptions.addOptimization(chrome_options)
    # chromeOptions.addMobile(chrome_options)

    # ChromeDriver를 webdriver_manager를 사용하여 자동으로 설치 및 설정
    service = Service(ChromeDriverManager().install())

    # Xvfb 설정
    os.environ['DISPLAY'] = ':99'

    # WebDriver 인스턴스 생성    
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver

def checkDriverStatus(driver):
    try:
        # Try to get the current URL
        current_url = driver.current_url
        print(f"Driver is running. Current URL: {current_url}")
    except WebDriverException as e:
        # If an exception occurs, it means the driver is not running
        print(f"Driver is not running. Exception: {e}")

    try:
        # Try to get the page title
        page_title = driver.title
        print(f"Driver is running. Page Title: {page_title}")
    except WebDriverException as e:
        # If an exception occurs, it means the driver is not running
        print(f"Driver is not running. Exception: {e}")

def findTargetByMidValueTest(driver, mid_value, isClick):
    find = False
    ranking = 0
    count = 1
    tryFinding = 0
    while not find or tryFinding < maxFind:
            find = findUtil.findByMidValue(driver, mid_value, isClick)
            print(f"height = {driver.execute_script("return document.body.scrollHeight")}")
            if find:
                page = count
                ranking = ranking + countUtil.getFindCountByMidValue(driver, mid_value)
                break
            else:
                ranking = ranking + countUtil.getCountAll(driver)
            for i in range(3, 11):
                try:
                    if count == maxPage:
                        element = allElements.getSearchInShopping(driver)
                        element.click()
                        time.sleep(1)
                        element = allElements.getSearchIconInShopping(driver)
                        element.click()
                        ranking = 0
                        count = 1
                        tryFinding = tryFinding + 1
                        break
                    # 찾는게 없으면 다음 버튼 클릭
                    if clickUtil.clickNext(driver, i):
                        print(f"clickNext({count}")
                        count = count + 1
                        break
                except:
                    continue
    return page, ranking

findProductByMidValue()