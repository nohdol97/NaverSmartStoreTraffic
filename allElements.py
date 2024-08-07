from selenium.webdriver.common.by import By

def getPlaceHolder(driver, placeHolder):
    return driver.find_element(By.XPATH, f'//*[@id="{placeHolder}"]')

def getShoppingPan(driver): # 네이버 모바일에서 검색창 아래 쇼핑판
    return driver.find_element(By.XPATH, '//*[@id="HOME_SHORTCUT"]/ul/li[2]/a/div/picture/img')

def getQuery(driver): # 네이버 모바일에서 검색창
    return driver.find_element(By.XPATH, '//*[@id="query"]')

def getSearchFake(driver): # 네이버 모바일에서 통합검색 위치
    return driver.find_element(By.XPATH, '//*[@id="MM_SEARCH_FAKE"]')

##### 쇼검 테스트 중...
def getShopping(driver): # 네이버 모바일 통합검색에서 검색창 아래 쇼핑 탭 (쇼핑투데이로 이동)
    return driver.find_element(By.XPATH, '//*[@id="_sch_tab"]/div//a[contains(text(), "쇼핑")]')

def getMoreShopping(driver): # 네이버 모바일 통합검색에서 '쇼핑 더보기' 버튼 (없을 수도 있음)
    return driver.find_element(By.XPATH, '//*[@id="ct"]//span[@class="kwd" and contains(text(), "쇼핑")]')

def getNaverHomeMoreTab(driver): # 네이버 모바일 홈에서 탭 더보기 (여기 내부에 있는 '네이버 쇼핑' 들어가야 함)
    return driver.find_element(By.XPATH, '//*[@id="HOME_SHORTCUT"]//a[contains(@href, "\\services.html")]')

def getEnterToNaverShoppingByHomeMoreTab(driver): # https://m.naver.com/services.html
    return driver.find_element(By.XPATH, '//*[@id="wrap"]//em[contains(text(), "네이버쇼핑")]')

def getLayerBottomSheet(driver):
    try:
        return driver.find_element(By.XPATH, '//*[@id="__next"]//button[contains(text(), "하루 동안 보지 않기")]')
    except:
        try:
            return driver.find_element(By.XPATH, '//*[@id="__next"]//span[contains(text(), "레이어 닫기")]')
        except:
            pass
    return None

def getSearchInShopping(driver): # 네이버 쇼핑 에서 검색창
    return driver.find_element(By.XPATH, '//*[@id="gnb-gnb"]//span[contains(text(), "상품명")]')

def getSearchInShoppingWeb(driver): # 네이버 쇼핑 웹 에서 검색창
    return driver.find_element(By.XPATH, '//*[@id="__next"]//input[@title="검색어 입력"]')

def getShoppingTabInShoppingPan(driver): # 네이버 모바일 쇼핑 탭으로 쇼핑투데이 진입 후 쇼핑 탭 이동
    return driver.find_element(By.XPATH, '//*[@id="NAV_LIST"]//*[@data-code="SHOP_VOGUE"]')

def getShoppingBestInShopping(driver): # 쇼핑 탭에서 best 탭
    return driver.find_element(By.XPATH, '//*[@id="mflick"]//a[@href="https://msearch.shopping.naver.com/best/home"]')

def getSearchInShoppingBest(driver):
    return driver.find_element(By.XPATH, "//button[.//span[contains(@class, 'blind') and normalize-space(text())='검색']]")

def getQueryInShopping(driver): # 네이버 쇼핑이랑 Best 등 곳에서 검색창
    return driver.find_element(By.XPATH, '//*[@id="input_text"]')
#####

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
        page_source = driver.page_source
        if "동시에 이용하는 이용자" in page_source or "사이트를 연결" in page_source or "쇼핑 서비스 접속" in page_source or "현재 서비스 접속" in page_source or "사이트에 연결" in page_source:
            return True
        return False
    except:
        return False

def findErrorForProduct(driver):
    try:
        page_source = driver.page_source
        if "동시에 이용하는 이용자" in page_source or "사이트를 연결" in page_source or "쇼핑 서비스 접속" in page_source or "현재 서비스 접속" in page_source:
            return True
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

def getSearchIconInShopping(driver):
    return driver.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div/div[1]/div[3]/button/svg')