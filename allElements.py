from selenium.webdriver.common.by import By

def getShoppingPan(driver): # 네이버 모바일에서 검색창 아래 쇼핑판
    return driver.find_element(By.XPATH, '//*[@id="HOME_SHORTCUT"]/ul/li[2]/a/div/picture/img')

def getQuery(driver): # 네이버 모바일에서 검색창
    return driver.find_element(By.XPATH, '//*[@id="query"]')

def getShopping(driver): # 네이버 모바일 통합검색에서 검색창 아래 쇼핑 탭
    return driver.find_element(By.XPATH, '//*[@id="_sch_tab"]/div//a[contains(text(), "쇼핑")]')

def getSearchFake(driver): # 네이버 모바일에서 통합검색 위치
    return driver.find_element(By.XPATH, '//*[@id="MM_SEARCH_FAKE"]')

def getMoreShopping(driver): # 네이버 모바일 통합검색에서 '쇼핑 더보기' 버튼 (없을 수도 있음)
    return driver.find_element(By.XPATH, '//*[@id="ct"]//span[@class="kwd" and contains(text(), "쇼핑")]')

def getNextButton(driver): # 네이버 모바일 쇼핑 내에서 다음 페이지 버튼
    return driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[9]/div/button[2]')

def getMidValueProduct(driver, mid_value): # 상품의 mid_value 로 위치 파악
    return driver.find_elements(By.XPATH, f'//*[@id="_sr_lst_{mid_value}"]/div/div[1]/a')

@DeprecationWarning
def getTitleValueProduct(driver, title): # 상품의 title 로 위치 파악
    return driver.find_elements(By.XPATH, f'//*[contains(text(), "{title}")]')

def getMoreDetailButton(driver): # 상품 페이지 내에서 '상세정보 펼쳐보기'
    return driver.find_element(By.XPATH, '//*[@id="INTRODUCE"]/div/div[5]/button')