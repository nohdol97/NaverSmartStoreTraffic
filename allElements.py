from selenium.webdriver.common.by import By

def getPlaceHolder(driver, placeHolder):
    return driver.find_element(By.XPATH, f'//*[@id="{placeHolder}"]')

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
    return driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[2]/div[{i}]/div/button[2]')

def getMidValueProduct(driver, mid_value, i): # 상품의 mid_value 로 위치 파악
    findAd = driver.find_elements(By.XPATH, f'//*[@id="_sr_lst_{mid_value}"]')
    for element in findAd:
        if '광고' not in element.text:
            child_a = element.find_element(By.XPATH, f'./div/div[{i}]/a')
            return child_a

def getPriceComparisonMidValueProduct(driver, mid_value): # 가격 비교 사이트 내에서 mid_value 로 위치 파악
    return driver.find_element(By.XPATH, f"//*[@id='section-price']//a[contains(@href, 'nvMid={mid_value}')]")

def getSellWhere(driver):
    return driver.find_element(By.XPATH, '//*[@id="__next"]//*[contains(text(), "판매처")]')

def getPriceComparisionMoreButton(driver): # 가격 비교 사이트 내에서 "전체 판매처 보러가기"
    return driver.find_element(By.XPATH, "//*[@id='section-price']//a[contains(@class, 'main_link_more')]")

def getPriceComparisionMoreMidValueProduct(driver, mid_value): # 가격 비교 사이트 내 전체 판매처 보러가기에서 mid_value 로 위치 파악
    return driver.find_element(By.XPATH, f"//*[@id='__next']//a[contains(@href, 'nvMid={mid_value}')]")

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
    try:
        # error_element = driver.find_element(By.XPATH, '//*[@id="main-message"]/h1/span')
        error_element = None # '사이트를 연결할 수 없습니다' 위에 부분인데 추가해야되나
        # /html/body 요소를 찾음
        element = driver.find_element(By.XPATH, '/html/body')
        
        # body_element 안에 <div class="content_error"> 요소가 있는지 확인
        naver_error_element = element.find_elements(By.CLASS_NAME, 'content_error')

        # content_error_divs 목록이 비어있지 않으면 True 반환
        if naver_error_element or error_element:
            return True
        else:
            return False
    except:
        return False

def findErrorForDetailProduct(driver):
    try:
        element = driver.find_element(By.CLASS_NAME, 'module_error') # 상품 들어갔을 때 '현재 서비스 접속이 불가합니다.'
        if element:
            return True
        else:
            return False
    except:
        return False

def getAllProduct(driver, i): # 네이버 모바일 쇼핑 내에서 모든 상품들 갯수 파악 위함
    return driver.find_elements(By.XPATH, f'//*[@id="__next"]/div/div[2]/div[{i}]/div/div[starts-with(@id, "_sr_lst")]')

def getSearchInShopping(driver):
    return driver.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div/div/div[1]/span')

def getSearchIconInShopping(driver):
    return driver.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div/div[1]/div[3]/button/svg')