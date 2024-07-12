from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver
import os, time, shutil
import chromeOptions

def create_driver(profileNum):
    for i in range(10):
        try:
            # 프로필 디렉토리 경로 지정
            original_profile_dir = os.path.join(os.getcwd(), f"chrome_profile{profileNum}")
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
            hiPaiProxy = chromeOptions.addProxy(chrome_options)

            # Xvfb 설정
            os.environ['DISPLAY'] = ':99'

            # ChromeDriver를 webdriver_manager를 사용하여 자동으로 설치 및 설정
            service = Service(ChromeDriverManager().install())

            # WebDriver 인스턴스 생성    
            driver = webdriver.Chrome(service=service, options=chrome_options)

            # Chrome 최적화
            # chromeOptions.intercept(driver)

            return driver, temp_profile_dir, hiPaiProxy
        except Exception as e:
            print(f"Error Creating driverInfo file: {e}")
            time.sleep(3)
            pass