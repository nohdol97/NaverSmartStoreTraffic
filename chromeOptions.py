from selenium.webdriver.common.proxy import Proxy, ProxyType
import hiPaiProxy

import mobile_emulations

def addOptimization(chrome_options, temp_profile_dir = None):
    chrome_options.add_argument("--log-level=3")  # ERROR 이상의 로그만 출력
    chrome_options.add_argument('--ignore-certificate-errors') # 인증서 오류 무시
    if temp_profile_dir:
        chrome_options.add_argument(f"--user-data-dir={temp_profile_dir}")  # 사용자 프로필 디렉토리 지정
    # chrome_options.add_argument('--disable-javascript')  # 자바스크립트 비활성화
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--no-zygote')
    chrome_options.add_argument('--disable-setuid-sandbox')
    # chrome_options.add_argument('--window-size=800,600')  # 해상도 최소화
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-popup-blocking')

    chrome_prefs = {
        "profile.managed_default_content_settings.images": 2,  # 이미지 비활성화
        "profile.managed_default_content_settings.videos": 2,  # 동영상 비활성화
        "profile.managed_default_content_settings.stylesheets": 2,  # 스타일시트 비활성화
    }
    chrome_options.add_experimental_option("prefs", chrome_prefs)

def addMobile(chrome_options):
    # mobile emulation (상품 상세 들어가면 모바일 아님)
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulations.getMobileEmulation())

def addProxy(chrome_options, ID = None):
    # hiPai Proxy 설정
    hiPaiIp = hiPaiProxy.getProxyIp(ID)
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = f"{hiPaiIp}"
    proxy.ssl_proxy = f"{hiPaiIp}"
    chrome_options.add_argument('--proxy-server=%s' % proxy.http_proxy)
    return hiPaiIp

# 너무 느려짐
def intercept(driver):
    # 캐시 저장소 초기화
    cached_responses = {}

    # 네트워크 인터셉터 추가: 이미지, 비디오, 폰트 및 스타일시트 요청 차단 및 캐시 활용
    def interceptor(request):
        if request.path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', 
                                  '.webp', '.mp4', '.mkv', '.webm', '.woff', 
                                  '.woff2', '.ttf', '.otf', '.css')):
            request.abort()
        else:
            # 캐시된 응답이 있는지 확인
            if request.url in cached_responses:
                cached_response = cached_responses[request.url]
                request.create_response(
                    status_code=200,
                    headers=cached_response['headers'].items(),
                    body=cached_response['body']
                )

    driver.request_interceptor = interceptor
    
    # 응답 가로채기: 캐시 저장
    def response_handler(request, response):
        cached_responses[request.url] = {
            'headers': dict(response.headers),
            'body': response.body
        }

    driver.response_interceptor = response_handler
    
    # 압축 응답 사용
    driver.header_overrides = {
        'Accept-Encoding': 'gzip, deflate, br'
    }