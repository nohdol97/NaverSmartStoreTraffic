import driverInfo
import util.clickUtil as clickUtil
import util.findUtil as findUtil
import util.loginUtil as loginUtil
import util.accessShoppingUtil as accessShoppingUtil
import util.cookieUtil as cookieUtil
import util.stayUtil as stayUtil
import productList

# ip 하나로 작업할 모든 상품 조회 하고, main 에서 ip 변경하고 작업
def mobileNaverShopping(proxy_ip):
    for mideValueKeywordStr in productList.getMidValueKeywordList():
        mid_value = mideValueKeywordStr.split(', ')[0]
        keyword = mideValueKeywordStr.split(', ')[1]

        driver = driverInfo.create_driver(proxy_ip)

        # 로그인 없이 키워드로 쇼핑 접속
        loginUtil.login_without_account(driver)

        # 쿠키 제거
        cookieUtil.deleteAllCookies(driver)

        # 쿠키 추가
        cookieUtil.getCookies(driver)

        # 쇼핑판, 상품 더 검색, 쇼핑
        accessShoppingUtil.access_random(driver, keyword)

        # 아래까지 스크롤 하면서 찾기
        find = False
        while not find:
            try:
                find = findUtil.findByMidValue(driver, mid_value)

                if find:
                    break
                for i in range(3, 11):
                    try:
                        # 찾는게 없으면 다음 버튼 클릭
                        if clickUtil.clickNext(driver, i):
                            break
                    except:
                        continue
            except:
                pass

        # 탭 전환
        tabs = driver.window_handles
        driver.switch_to.window(tabs[-1])

        # 찾은 상세페이지 체류
        stayUtil.stay_target(driver)