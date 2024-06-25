from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver
import OxyLabsProxy

def create_driver():
    # 프록시 설정
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--log-level=3")  # ERROR 이상의 로그만 출력
    chrome_options.add_argument('--ignore-certificate-errors') # 인증서 오류 무시
    chrome_prefs = {
        "profile.managed_default_content_settings.images": 2,  # 이미지 비활성화
        "profile.managed_default_content_settings.video": 2    # 동영상 비활성화
    }
    chrome_options.add_experimental_option("prefs", chrome_prefs)
    # proxies = OxyLabsProxy.getProxies()

    # ChromeDriver를 webdriver_manager를 사용하여 자동으로 설치 및 설정
    service = Service(ChromeDriverManager().install())
    
    # WebDriver 인스턴스 생성
    # driver = webdriver.Chrome(service=service, options=chrome_options, seleniumwire_options=proxies)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver