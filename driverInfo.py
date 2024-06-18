from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def create_driver(proxy_ip):
    # 프록시 설정
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")  # ERROR 이상의 로그만 출력
    # chrome_options.add_argument('--proxy-server=%s' % proxy_ip) # 프록시 설정

    # ChromeDriver를 webdriver_manager를 사용하여 자동으로 설치 및 설정
    service = Service(ChromeDriverManager().install())
    
    # WebDriver 인스턴스 생성
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver