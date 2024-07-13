from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver  # seleniumwire로 변경
import os, time, shutil, psutil
import chromeOptions
import hiPaiProxy
import cacheMaker

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

            # seleniumwire 옵션 설정
            current_dir = os.path.dirname(os.path.abspath(__file__))
            cert_path = os.path.join(current_dir, 'selenium_ssl', 'ca.crt')
            key_path = os.path.join(current_dir, 'selenium_ssl', 'ca.key')
            seleniumwire_options = {
                'ca_cert': cert_path,
                'ca_key': key_path
            }

            # WebDriver 인스턴스 생성    
            driver = webdriver.Chrome(service=service, options=chrome_options, seleniumwire_options=seleniumwire_options)

            # Chrome 최적화
            # chromeOptions.intercept(driver)

            return driver, temp_profile_dir, hiPaiProxy
        except Exception as e:
            print(f"Error Creating driverInfo file: {e}")
            time.sleep(3)
            pass

def make_driver(profileNum):
    for i in range(10):
        try:
            driver, temp_profile_dir, proxy = create_driver(profileNum)
            return driver, temp_profile_dir, proxy
        except Exception as e:
            hiPaiProxy.addProxyIp(proxy)
            kill_driver(driver)
            cacheMaker.create_cache(profileNum)
            print(f"Error: {e}")
            time.sleep(3)

def kill_driver(driver, proxy):
    try:
        if driver.service.process:  # 프로세스가 존재하는지 확인
            driver.quit()
            time.sleep(2)  # 프로세스가 종료될 시간을 충분히 줌
            if proxy:
                hiPaiProxy.addProxyIp(proxy)
    except Exception as e:
        print(f"Error while quitting the driver: {e}")
        try:
            process = psutil.Process(driver.service.process.pid)
            for proc in process.children(recursive=True):
                proc.kill()
            process.kill()
            time.sleep(2)
            if proxy:
                hiPaiProxy.addProxyIp(proxy)
            print("Driver process killed successfully.")
        except Exception as e:
            print(f"Error while killing the driver process: {e}")