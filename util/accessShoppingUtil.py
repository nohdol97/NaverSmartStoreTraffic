import time
from selenium.webdriver.common.keys import Keys

import timeValues as timeValues
import util.randomUtil as randomUtil
import allElements

def access_direct(driver, keyword):
    url = f"https://msearch.shopping.naver.com/search/all?query={keyword}"
    driver.get(url)
    # driver 에 해당 ip 접근 불가 있으면 return False
    if allElements.findError(driver):
        return False
    return True

def access_total_random(driver, keyword):
    randomValue = randomUtil.get_random_value()
    try:
        # if randomValue < 0.3: # 30퍼 확률
        #     access_by_shoppingPan(driver, keyword)
        if randomValue < 0.6: # 30퍼 확률
            access_by_totalSearch_shopping(driver, keyword)
        else: # 40퍼 확률
            access_by_totalSearch_more_shopping(driver, keyword)
        # if allElements.findError(driver):
        #     return False
        # return True
        if allElements.findError(driver):
            return False
        return True
    except:
        url = "https://m.naver.com/"
        driver.get(url)
        access_by_totalSearch_shopping(driver, keyword)
        # if allElements.findError(driver):
        #     return False
        # return True
        if allElements.findError(driver):
            return False
        return True

def access_by_totalSearch_shopping(driver, keyword):
    driver.get("https://m.naver.com/")
    # 검색창 클릭
    element = allElements.getSearchFake(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())

    # 키워드 검색
    element = allElements.getQuery(driver)
    element.send_keys(keyword)
    element.send_keys(Keys.ENTER)
    time.sleep(timeValues.getWaitLoadingTime())

    # 쇼핑 클릭
    element = allElements.getShopping(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())

def access_by_totalSearch_more_shopping(driver, keyword):
    driver.get("https://m.naver.com/")
    # 검색창 클릭
    element = allElements.getSearchFake(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())

    # 키워드 검색
    element = allElements.getQuery(driver)
    element.send_keys(keyword)
    element.send_keys(Keys.ENTER)
    time.sleep(timeValues.getWaitLoadingTime())

    # 쇼핑 더보기 클릭
    element = allElements.getMoreShopping(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())

def access_by_shopping(driver, keyword):
    # driver.get("https://shopping.naver.com/home")
    # https://m.naver.com/services.html
    driver.get("https://m.naver.com/")
    driver.get("https://m.naver.com/services.html")

    # 네이버 쇼핑 이동 (https://shopping.naver.com/home)
    element = allElements.getEnterToNaverShoppingByHomeMoreTab(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())
    
    # BottomSheet 있으면 닫음
    for i in range(3):
        element = allElements.getLayerBottomSheet(driver)
        if element:
            element.click()
            time.sleep(timeValues.getWaitLoadingTime())
            break

    # 검색창 클릭
    for i in range(3):
        element = allElements.getSearchInShopping(driver)
        if element:
            element.click()
            time.sleep(timeValues.getWaitLoadingTime())
            break

    for i in range(3):
        element = allElements.getSearchInShoppingWeb(driver)
        if element:
            element.click()
            time.sleep(timeValues.getWaitLoadingTime())
            break

    # 키워드 검색
    element = allElements.getQueryInShopping(driver)
    element.send_keys(keyword)
    element.send_keys(Keys.ENTER)
    time.sleep(timeValues.getWaitLoadingTime())

def access_by_shopping_best(driver, keyword):
    driver.get("https://m.naver.com/")
    # 쇼핑판 클릭
    element = allElements.getShoppingPan(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())

    # 쇼핑 투데이에서 쇼핑 탭 클릭
    element = allElements.getShoppingTabInShoppingPan(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())

    # 쇼핑 탭에서 best 클릭
    element = allElements.getShoppingBestInShopping(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())

    # 검색창 클릭
    element = allElements.getSearchInShoppingBest(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())
    
    # 키워드 검색
    element = allElements.getQueryInShoppingBest(driver)
    element.send_keys(keyword)
    element.send_keys(Keys.ENTER)
    time.sleep(timeValues.getWaitLoadingTime())

def access_by_imageShopping(driver, url):
    driver.get("https://m.naver.com/")
    driver.get(url)
    time.sleep(timeValues.getWaitImageProductLoadingTime())
    element = allElements.getImageProduct(driver)
    element.click()
    time.sleep(timeValues.getWaitLoadingTime())