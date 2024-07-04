import util.findUtil as findUtil
import util.accessShoppingUtil as accessShoppingUtil
import util.stayUtil as stayUtil
import allElements

import time

# ip 하나로 작업할 모든 상품 조회 하고, main 에서 ip 변경하고 작업
def mobileNaverShopping(driver, mid_value, keyword):
    # 쇼핑판(불가), 상품 더 검색, 쇼핑
    accessShoppingUtil.access_random(driver, keyword)

    # driver 에 해당 ip 접근 불가 있으면 return False
    if allElements.findError(driver):
        return False

    # 아래까지 스크롤 하면서 찾기
    page, ranking = findUtil.findTargetByMidValue(driver, mid_value, True)
    
    print(f"mid_value({mid_value}), ranking({ranking})")

    # 탭 전환
    # driver.close()
    # tabs = driver.window_handles
    # driver.switch_to.window(tabs[-1])

    # 찾은 상세페이지 체류
    stayUtil.stay_target(driver)
    return True

# 해당 링크 아래 정보가 나오지 않음 (driverInfo 자바스크립트 비활성화 때문인듯)
# https://search.naver.com/search.naver?ssc=tab.image.all&where=image&query=%22%ED%8B%B0%EB%B9%84+%EC%8A%A4%ED%83%A0%EB%93%9C+%EC%82%BC%ED%83%A0%EB%B0%94%EC%9D%B4%EB%AF%B8+%EC%9D%B4%EB%8F%99%EC%8B%9D+%EA%B1%B0%EC%B9%98%EB%8C%80+LG+%EC%82%BC%EC%84%B1+%EC%A4%91%EC%86%8C+%EB%B2%A0%EC%82%AC%ED%99%80+100%ED%98%B8%ED%99%98%22&sm=tab_dgs&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall#imgId=image_sas%3Anshopping_fd30779427f7287b35484c52e5d84bea
def mobileNaverImageShopping(driver, url):
    accessShoppingUtil.access_by_imageShopping(driver, url)

    # 찾은 상세페이지 체류
    stayUtil.stay_target(driver)