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

def getNextButton(driver, i): # 네이버 모바일 쇼핑 내에서 다음 페이지 버튼
    return driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[2]/div[{8}]/div/button[2]')

def getMidValueProduct(driver, mid_value, i): # 상품의 mid_value 로 위치 파악
    return driver.find_elements(By.XPATH, f'//*[@id="_sr_lst_{mid_value}"]/div/div[{i}]/a')

@DeprecationWarning
def getTitleValueProduct(driver, title): # 상품의 title 로 위치 파악
    return driver.find_elements(By.XPATH, f'//*[contains(text(), "{title}")]')

def getMoreDetailButton(driver, i): # 상품 페이지 내에서 '상세정보 펼쳐보기' 
    return driver.find_element(By.XPATH, f'//*[@id="INTRODUCE"]/div/div[{i}]/button')

def getStayLoginState(driver): # 로그인 유지하기 버튼
    return driver.find_element(By.XPATH, '//*[@id="login_stay"]/label')

def getImageProduct(driver): # 이미지 "상품 바로가기" 버튼
    return driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[1]/div[3]/div[1]/div/div[2]/div/div/a[1]')

def findError(driver):
    # /html/body 요소를 찾음
    body_element = driver.find_element(By.XPATH, '/html/body')
    
    # body_element 안에 <div class="content_error"> 요소가 있는지 확인
    content_error_divs = body_element.find_elements(By.CLASS_NAME, 'content_error')

    # content_error_divs 목록이 비어있지 않으면 True 반환
    if content_error_divs:
        return True
    else:
        return False
    
def getAllProduct(driver, i): # 네이버 모바일 쇼핑 내에서 모든 상품들 갯수 파악 위함
    return driver.find_elements(By.XPATH, f'//*[@id="__next"]/div/div[2]/div[{i}]/div/div[starts-with(@id, "_sr_lst")]')

def getSearchInShopping(driver):
    return driver.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div/div/div[1]/span')

def getSearchIconInShopping(driver):
    return driver.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div/div[1]/div[3]/button/svg')