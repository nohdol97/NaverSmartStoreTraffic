import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import allElements

def scrollEndPosition(driver):
    document_height = int(driver.execute_script("return document.body.scrollHeight"))
    now_scroll_height = int(driver.execute_script("return window.scrollY + window.innerHeight"))
    return now_scroll_height < document_height
    
def scrollToEndFast(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    for i in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height

def scrollToEnd(driver, scrollIntervalTime):
    while scrollEndPosition(driver):
        driver.find_element(By.XPATH, "//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(scrollIntervalTime)

def scrollDetailPage(driver, scrollIntervalTime):
    while scrollEndPosition(driver):
        driver.find_element(By.XPATH, "//body").send_keys(Keys.PAGE_DOWN)
        time.sleep(scrollIntervalTime)
        try:
            for i in range(3, 10):
                try:
                    # 더보기 버튼 요소 찾기
                    button_element = allElements.getMoreDetailButton(driver, i)
                    if button_element:
                        break
                except:
                    continue
    
            # 요소 위치 가져오기
            button_location = button_element.location

            # 현재 스크롤 위치와 보이는 화면 높이 가져오기
            current_scroll_position = driver.execute_script("return window.pageYOffset;")
            window_height = driver.execute_script("return window.innerHeight;")

            # 요소가 보이는 화면 내에 있는지 확인
            if current_scroll_position <= button_location['y'] <= (current_scroll_position + window_height):
                # 요소 클릭
                button_element.click()
                time.sleep(scrollIntervalTime)
        except:
            pass