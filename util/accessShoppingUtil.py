import time
from selenium.webdriver.common.keys import Keys

import timeValues as timeValues
import util.randomUtil as randomUtil
import allElements

def access_random(driver, keyword):
    randomValue = randomUtil.get_random_value()
    try:
        # if randomValue < 0.3: # 30퍼 확률
        #     access_by_shoppingPan(driver, keyword)
        if randomValue < 0.6: # 30퍼 확률
            access_by_totalSearch_shopping(driver, keyword)
        else: # 40퍼 확률
            access_by_totalSearch_more_shopping(driver, keyword)
    except:
        url = "https://m.naver.com/"
        driver.get(url)
        access_by_totalSearch_shopping(driver, keyword)

def access_by_shoppingPan(driver, keyword):
    # 쇼핑판 클릭
    element = allElements.getShoppingPan(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())

    # 검색창 클릭
    element = allElements.getQuery(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())
    
    # 키워드 검색
    search_box = allElements.getQuery(driver)
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.ENTER)
    time.sleep(timeValues.getWaitLoadingTime())

    # 쇼핑 클릭
    element = allElements.getShopping(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())

def access_by_totalSearch_shopping(driver, keyword):
    # 검색창 클릭
    element = allElements.getSearchFake(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())

    # 키워드 검색
    search_box = allElements.getQuery(driver)
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.ENTER)
    time.sleep(timeValues.getWaitLoadingTime())

    # 쇼핑 클릭
    element = allElements.getShopping(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())

def access_by_totalSearch_more_shopping(driver, keyword):
    # 검색창 클릭
    element = allElements.getSearchFake(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())

    # 키워드 검색
    search_box = allElements.getQuery(driver)
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.ENTER)
    time.sleep(timeValues.getWaitLoadingTime())

    # 쇼핑 더보기 클릭
    element = allElements.getMoreShopping(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())

def access_by_imageShopping(driver, url):
    driver.get(url)
    time.sleep(timeValues.getWaitImageProductLoadingTime())
    element = allElements.getImageProduct(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())