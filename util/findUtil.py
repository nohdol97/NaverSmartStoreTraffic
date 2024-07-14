import time

import timeValues as timeValues
import util.scrollUtil as scrollUtil
import util.countUtil as countUtil
import util.clickUtil as clickUtil
import util.loginUtil as loginUtil
import util.accessShoppingUtil as accessShoppingUtil

import allElements
import setValues

def findTargetByMidValue(driver, mid_value, keyword, isPriceComparisonSite, isClick):
    find = False
    ranking = 0
    count = 1
    tryFinding = 0
    isInMorePriceComarisonSite = False
    while not find and tryFinding < setValues.maxAttempts:
        find = findByMidValue(driver, mid_value, isPriceComparisonSite, isInMorePriceComarisonSite, isClick)
        if find:
            time.sleep(3)
            page = count
            try:
                ranking = ranking + countUtil.getFindCountByMidValue(driver, mid_value)
            except:
                return find, page, ranking
            return find, page, ranking
        else:
            ranking = ranking + countUtil.getCountAll(driver)
        if not isPriceComparisonSite:
            for i in range(1, 11):
                try:
                    if count == setValues.maxPages:
                        accessShoppingUtil.access_direct(driver, keyword)
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
        else:
            tryFinding = tryFinding + 1
            # raise ValueError('가격 비교 사이트 내에서 "전체 판매처 보러가기" 현재 새탭에서 열려서 문제')
            # try:
            #     element = findMoreProductButtonInPriceComparisonSite(driver)
            #     isInMorePriceComarisonSite = True
            #     tryFinding = tryFinding + 1
            # except:
            #     pass
    return find, None, None

def findMoreProductButtonInPriceComparisonSite(driver):
    element = allElements.getSellWhere(driver)
    element.click()
    time.sleep(1)
    element = allElements.getPriceComparisionMoreButton(driver)
    if element:
        # 있다면 해당 버튼 위치로 이동
        element_location = element.location['y']
        offset = -150  # 요소 위치에서 위로 스크롤할 픽셀 값
        driver.execute_script(f"window.scrollTo(0, {element_location + offset});")
        time.sleep(timeValues.getWaitLoadingTime())

        clickUtil.clickTarget(driver, element) # 현재 탭에서 열기 TODO 새 탭에서 열리고 있어서 수정 필요
        return element
    
def findByMidValue(driver, mid_value, isPriceComparisonSite, isInMorePriceComarisonSite, isClick):
    # 맨 아래로 빠르게 스크롤
    scrollUtil.scrollToEndFast(driver)
    
    # mid_value 기준 해당 상품 있는지 확인
    time.sleep(timeValues.getWaitScrollTime())
    try:
        for i in range(1, 5):
            if isPriceComparisonSite and isInMorePriceComarisonSite:
                element = allElements.getPriceComparisionMoreMidValueProduct(driver, mid_value)
            elif isPriceComparisonSite:
                element = allElements.getPriceComparisonMidValueProduct(driver, mid_value)
            else:
                element = allElements.getMidValueProduct(driver, mid_value, i)
            if element:
                # 있다면 해당 상품 위치로 이동
                element_location = element.location['y']
                offset = -150  # 요소 위치에서 위로 스크롤할 픽셀 값
                driver.execute_script(f"window.scrollTo(0, {element_location + offset});")
                time.sleep(timeValues.getWaitLoadingTime())
                if isClick: # cache 만들때는 클릭 안함
                    clickUtil.clickTarget(driver, element)
                return element
    except:
        return False

@DeprecationWarning
def findByTitle(driver, title):
    while scrollUtil.scrollEndPosition(driver):
        # 맨 아래로 빠르게 스크롤
        scrollUtil.scrollToEndFast(driver)

        # title 기준 해당 상품 있는지 확인
        element = allElements.getTitleValueProduct(driver, title)
        if element:
            # 있다면 해당 상품 위치로 이동
            element_location = element.location['y']
            offset = -150  # 요소 위치에서 위로 스크롤할 픽셀 값
            driver.execute_script(f"window.scrollTo(0, {element_location + offset});")
            time.sleep(timeValues.getWaitLoadingTime())
            
            clickUtil.clickTarget(driver, element)
            return element