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
import chromeOptions

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
        mid_value, keyword = line.split(',')
        print(f"midValue({mid_value}), keyword({keyword})")
        url = f"https://msearch.shopping.naver.com/search/all?query={keyword}"

        print("driver get E")
        driver.get(url)
        print("driver get X")
        time.sleep(3)

        driver.save_screenshot('/home/ubuntu/screenshot1.png')
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

findProductByMidValue()