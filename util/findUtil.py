import time, re

import timeValues as timeValues
import util.scrollUtil as scrollUtil
import util.countUtil as countUtil
import util.clickUtil as clickUtil

import allElements

maxPage = 20
maxFind = 3

def findTargetByMidValue(driver, mid_value, isClick):
    find = False
    ranking = 0
    count = 1
    tryFinding = 0
    while not find or tryFinding < maxFind:
            find = findByMidValue(driver, mid_value, isClick)
            if find:
                page = count
                ranking = ranking + countUtil.getFindCountByMidValue(driver, mid_value)
                break
            else:
                ranking = ranking + countUtil.getCountAll(driver)
            for i in range(3, 11):
                try:
                    if count == maxPage:
                        element = allElements.getSearchInShopping(driver)
                        element.click()
                        time.sleep(1)
                        element = allElements.getSearchIconInShopping(driver)
                        element.click()
                        ranking = 0
                        count = 1
                        tryFinding = tryFinding + 1
                        break
                    # 찾는게 없으면 다음 버튼 클릭
                    if clickUtil.clickNext(driver, i):
                        count = count + 1
                        break
                except:
                    continue
    return page, ranking

def findByMidValue(driver, mid_value, isClick):
    # 맨 아래로 빠르게 스크롤
    scrollUtil.scrollToEndFast(driver)
    
    # mid_value 기준 해당 상품 있는지 확인
    time.sleep(timeValues.getWaitScrollTime())
    for i in range(1, 5):
        elements = allElements.getMidValueProduct(driver, mid_value, i)
        if elements:
            # 있다면 해당 상품 위치로 이동
            element_location = elements[0].location['y']
            offset = -150  # 요소 위치에서 위로 스크롤할 픽셀 값
            driver.execute_script(f"window.scrollTo(0, {element_location + offset});")
            time.sleep(timeValues.getWaitLoadingTime())
            
            if isClick:
                clickUtil.clickTarget(driver, elements)
            return elements

@DeprecationWarning
def findByTitle(driver, title, isClick):
    while scrollUtil.scrollEndPosition(driver):
        # 맨 아래로 빠르게 스크롤
        scrollUtil.scrollToEndFast(driver)

        # title 기준 해당 상품 있는지 확인
        elements = allElements.getTitleValueProduct(driver, title)
        if elements:
            # 있다면 해당 상품 위치로 이동
            element_location = elements[0].location['y']
            offset = -150  # 요소 위치에서 위로 스크롤할 픽셀 값
            driver.execute_script(f"window.scrollTo(0, {element_location + offset});")
            time.sleep(timeValues.getWaitLoadingTime())
            
            if isClick:
                clickUtil.clickTarget(driver, elements)
            return elements