import time

import timeValues as timeValues
import util.scrollUtil as scrollUtil
import allElements

def findByMidValue(driver, mid_value):
    # 맨 아래로 빠르게 스크롤
    scrollUtil.scrollToEndFast(driver)
    
    # mid_value 기준 해당 상품 있는지 확인
    time.sleep(timeValues.getWaitScrollTime())
    elements = allElements.getMidValueProduct(driver, mid_value)
    if elements:
        # 있다면 해당 상품 위치로 이동
        element_location = elements[0].location['y']
        offset = -150  # 요소 위치에서 위로 스크롤할 픽셀 값
        driver.execute_script(f"window.scrollTo(0, {element_location + offset});")
        time.sleep(timeValues.getWaitLoadingTime())
        try:
            # 상품 클릭 시도
            elements[0].click()
            return True
        except Exception as e:
            # 가려져 있는 요소 찾기
            overlapping_element = driver.execute_script("""
                var elem = arguments[0];
                var rect = elem.getBoundingClientRect();
                return document.elementFromPoint(rect.left + rect.width / 2, rect.top + rect.height / 2);
            """, elements[0])
            
            # 가려져 있는 요소 클릭
            driver.execute_script("arguments[0].click();", overlapping_element)
            return True

@DeprecationWarning
def findByTitle(driver, title):
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
            try:
                # 상품 클릭 시도
                elements[0].click()
                return True
            except Exception as e:
                # 가려져 있는 요소 찾기
                overlapping_element = driver.execute_script("""
                    var elem = arguments[0];
                    var rect = elem.getBoundingClientRect();
                    return document.elementFromPoint(rect.left + rect.width / 2, rect.top + rect.height / 2);
                """, elements[0])
                
                # 가려져 있는 요소 클릭
                driver.execute_script("arguments[0].click();", overlapping_element)
                return True