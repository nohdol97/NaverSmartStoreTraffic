from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver
import os, random

def create_cache(urls, cache_number):
    profile_dir = os.path.join(os.getcwd(), f"chrome_profile{cache_number}")

    # 프로필 디렉토리 생성
    if not os.path.exists(profile_dir):
        os.makedirs(profile_dir)

    # 프록시 설정
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--log-level=3")  # ERROR 이상의 로그만 출력
    chrome_options.add_argument(f"user-data-dir={profile_dir}")  # 사용자 프로필 디렉토리 지정
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--no-zygote')
    chrome_options.add_argument('--disable-setuid-sandbox')
    chrome_options.add_argument('--window-size=800,600')  # 해상도 최소화
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('--headless')  # 헤드리스 모드
    chrome_prefs = {
        "profile.managed_default_content_settings.images": 2,  # 이미지 비활성화
        "profile.managed_default_content_settings.videos": 2,  # 동영상 비활성화
        "profile.managed_default_content_settings.stylesheets": 2,  # 스타일시트 비활성화
    }
    chrome_options.add_experimental_option("prefs", chrome_prefs)

    # ChromeDriver를 webdriver_manager를 사용하여 자동으로 설치 및 설정
    service = Service(ChromeDriverManager().install())
    
    # WebDriver 인스턴스 생성
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # 랜덤한 개수의 랜덤한 URL 선택
    num_urls = random.randint(7, len(urls))  # 7부터 urls 리스트의 길이까지 랜덤한 개수 선택
    selected_urls = random.sample(urls, num_urls)  # 랜덤한 URL들을 선택

    for url in selected_urls:
        try:
            driver.set_page_load_timeout(10)  # 페이지 로딩 타임아웃 설정 (초)
            driver.get(url)
        except:
            pass

    # 드라이버 종료
    driver.quit()

# 방문할 url (변경하면서 사용)
urls = [
    "https://m.naver.com/",
    "https://m.blog.naver.com/Recommendation.naver",
    "https://m.sports.naver.com/scoreboard/index",
    "https://m.coupang.com/",
    "https://xn--939au0g4vj8sq.net/",
    "https://m.entertain.naver.com/home",
    "https://m.entertain.naver.com/movie",
    "https://m.stock.naver.com/domestic/top/total",
    "https://m.comic.naver.com/index",
    "https://m.11st.co.kr/",
    "https://m.gmarket.co.kr/",
    "https://m.auction.co.kr/",
    "https://m.interpark.com/",
    "https://m.wemakeprice.com/",
    "https://m.tmon.co.kr/",
    "https://m.kurly.com/shop/main/index.php",
    "https://m.ssg.com/",
    "https://m.daisomall.co.kr/",
    "https://m.daum.net/",
    "https://m.news.naver.com/",
    "https://m.dcinside.com/",
    "https://m.ppomppu.co.kr/",
    "https://m.instiz.net/",
    "https://m.fmkorea.com/",
    "https://m.music.bugs.co.kr/",
    "https://m.melon.com/",
    "https://m.vlive.tv/",
    "https://m.cafe.daum.net/",
    "https://m.mega.nate.com/",
    "https://m.inven.co.kr/",
    "https://m.clien.net/",
    "https://m.ruliweb.com/",
    "https://m.twitch.tv/",
    "https://m.chosun.com/",
    "https://m.joins.com/",
    "https://m.donga.com/",
    "https://m.hani.co.kr/",
    "https://m.hankyung.com/",
    "https://m.pann.nate.com/",
    "https://m.ilbe.com/",
    "https://m.humoruniv.com/",
    "https://m.theqoo.net/",
    "https://m.mlbdraftk.com/",
    "https://m.kbs.co.kr/",
    "https://m.sbs.co.kr/",
    "https://m.mbc.co.kr/",
    "https://m.ebs.co.kr/",
    "https://m.cjenm.com/",
    "https://m.lotteworld.com/",
    "https://m.cyworld.com/",
    "https://m.hangame.com/",
    "https://m.gmarket.co.kr/",
    "https://m.oliveyoung.co.kr/",
    "https://m.naver.com/",
    "https://m.pandora.tv/"
]

for cache_number in range(1, 11): # 1부터 10까지 만듦
    create_cache(urls, cache_number)