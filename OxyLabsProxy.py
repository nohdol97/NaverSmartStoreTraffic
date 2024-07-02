import re
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = "customer-nohdol_CoH8a-cc-kr"
PASSWORD = "Rkddkwlvnf0_"
ENDPOINT = "kr-pr.oxylabs.io:30000"
# socks5h://customer-nohdol_CoH8a-cc-kr:Rkddkwlvnf0_@pr.oxylabs.io:7777

def chrome_proxy(user: str, password: str, endpoint: str) -> dict:
    wire_options = {
        "proxy": {
            "http": f"http://{user}:{password}@{endpoint}",
            "https": f"https://{user}:{password}@{endpoint}",
        },
    }

    return wire_options

def getProxies():
    proxies = chrome_proxy(USERNAME, PASSWORD, ENDPOINT)
    return proxies

# for test
def get_ip_via_chrome():
    manage_driver = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.headless = True
    proxies = chrome_proxy(USERNAME, PASSWORD, ENDPOINT)
    driver = webdriver.Chrome(
        service=manage_driver, options=options, seleniumwire_options=proxies
    )
    try:
        driver.get("https://m.naver.com/")
        ip_pattern = r"[0-9]+(?:\.[0-9]+){3}"
        match = re.search(ip_pattern, driver.page_source)
        if match:
            return f'\nYour IP is: {match.group()}'
        else:
            return "No IP address found in the page source."
    finally:
        driver.quit()