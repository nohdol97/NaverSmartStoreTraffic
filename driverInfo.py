from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver
import os, random, shutil
import chromeOptions, OxyLabsProxy

previous_number = None

def get_new_cache_number(previous_number):
    numbers = list(range(1, 11))  # 1부터 10까지의 숫자를 생성
    if previous_number in numbers:
        numbers.remove(previous_number)
    return random.choice(numbers)

def create_driver(profileNum, ID = None):
    # 프로필 디렉토리 경로 지정
    global previous_number
    cache_number = get_new_cache_number(previous_number)
    original_profile_dir = os.path.join(os.getcwd(), f"chrome_profile{cache_number}")
    temp_profile_dir = os.path.join(os.getcwd(), f"temp_chrome_profile{profileNum}")

    # 기존 임시 프로필 디렉토리가 있다면 삭제
    if os.path.exists(temp_profile_dir):
        shutil.rmtree(temp_profile_dir)

    # 원본 프로필 디렉토리를 임시 디렉토리로 복사
    shutil.copytree(original_profile_dir, temp_profile_dir)

    # Chrome option 설정
    chrome_options = webdriver.ChromeOptions()
    chromeOptions.addOptimization(chrome_options, temp_profile_dir)
    chromeOptions.addMobile(chrome_options)
    isLogin = chromeOptions.addProxy(chrome_options, ID)

    # ChromeDriver를 webdriver_manager를 사용하여 자동으로 설치 및 설정
    service = Service(ChromeDriverManager().install())

    # WebDriver 인스턴스 생성    
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Chrome 최적화
    # chromeOptions.intercept(driver)

    return driver, temp_profile_dir, isLogin