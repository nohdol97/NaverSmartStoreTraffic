import time, os, sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip as pp
from random import uniform

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from timeValues import getWaitLoadingTime
import allElements

def naverHome(driver):
    # 네이버 모바일 페이지 접속
    url = "https://m.naver.com/"
    driver.get(url)

def inputkeys(driver, someWord : str, placeholder : str):
    pp.copy(someWord)
    holderInput = driver.find_element(By.XPATH, f"//input[@placeholder='{placeholder}']")
    holderInput.click()
    pp.copy(someWord)
    time.sleep(uniform(1.0, 2.0))
    
    # 윈도우 환경에서 붙여넣기
    holderInput.send_keys(Keys.CONTROL, 'v')
    
    # 맥 환경에서 붙여넣기
    # holderInput.send_keys(Keys.COMMAND, 'v')

def login_with_account(driver, naverid, naverpassword):
    fail_login = False
    # 로그인 2번 시도
    for i in range(2):
        if i == 1 and fail_login == False:
            break
        driver.get("https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/")
        time.sleep(2)
        inputkeys(driver, naverid, "아이디")
        inputkeys(driver, naverpassword, "비밀번호")
        try:
            element = allElements.getStayLoginState(driver)
            element.click()
        except:
            pass
        time.sleep(1)
        driver.find_element(By.XPATH, f"//input[@placeholder='비밀번호']").send_keys(Keys.ENTER)
        time.sleep(1)
        fail_login = failLogin(driver)

def failLogin(driver):
    try:
        driver.find_element(By.XPATH, '//*[@id="error_message"]')
        return True
    except:
        return False

def update_account_status(account_line):
    with open('accounts.txt', 'r') as file:
        lines = file.readlines()

    with open('accounts.txt', 'w') as file:
        for line in lines:
            if line.strip() == account_line.strip():
                file.write(f'{line.strip()},used\n')
            else:
                file.write(line)