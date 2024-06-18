import time

import util.randomUtil as randomUtil
import timeValues as timeValues

def deleteAllCookies(driver):
    driver.delete_all_cookies()

def getCookies(driver):
    cookies = []
    randomValue = randomUtil.get_random_value()
    if randomValue < 0.3: # 30퍼 확률
        driver.get('https://m.entertain.naver.com/home')
        time.sleep(timeValues.getWaitLoadingTime())  # 각 접속 사이에 대기
        driver.get('https://m.naver.com/')
        time.sleep(timeValues.getWaitLoadingTime())  # 각 접속 사이에 대기
    elif randomValue < 0.6: # 30퍼 확률
        driver.get('https://m.sports.naver.com/scoreboard/index')
        time.sleep(timeValues.getWaitLoadingTime())  # 각 접속 사이에 대기
        driver.get('https://m.naver.com/')
        time.sleep(timeValues.getWaitLoadingTime())  # 각 접속 사이에 대기
    else: # 40퍼 확률
        driver.get('https://m.entertain.naver.com/home')
        time.sleep(timeValues.getWaitLoadingTime())  # 각 접속 사이에 대기
        driver.get('https://m.sports.naver.com/scoreboard/index')
        time.sleep(timeValues.getWaitLoadingTime())  # 각 접속 사이에 대기
        driver.get('https://m.naver.com/')
        time.sleep(timeValues.getWaitLoadingTime())  # 각 접속 사이에 대기
    return cookies