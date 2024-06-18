import time

import timeValues as timeValues

def login_without_account(driver):
    # 네이버 모바일 페이지 접속
    url = "https://m.naver.com/"
    driver.get(url)
    time.sleep(timeValues.getWaitLoadingTime())  # 페이지 로딩 대기

def login_with_account(driver):
    pass