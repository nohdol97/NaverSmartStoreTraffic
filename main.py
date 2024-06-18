import time
import proxy
import work
import timeValues as timeValues
import traceback

# TODO: Proxy IP 셋팅되면 proxy_list 에 넣고 사용
# proxies = proxy.getProxyList()
proxies = [
    1
]

# 각 프록시를 사용하여 네이버 페이지 접속 테스트
for proxy in proxies:
    try:
        work.mobileNaverShopping(proxy)
    except Exception as e:
        print(f"Proxy: {proxy} - Error: {e}")
        traceback.print_exc()
    time.sleep(timeValues.getWaitLoadingTime())  # 각 접속 사이에 대기