import re
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import base64

USERNAME = "nohdol_HlzdL"
PASSWORD = "Rkddkwlvnf0_"
ENDPOINT = "unblock.oxylabs.io:60000"

def chrome_proxy(user: str, password: str, endpoint: str) -> dict:
    wire_options = {
        "proxy": {
            "http": f"http://{user}:{password}@{endpoint}",
            "https": f"https://{user}:{password}@{endpoint}",
        },
        # "headers": {
        #     "x-oxylabs-geo-location": "Korea"
        # }
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

get_ip_via_chrome()