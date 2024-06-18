import random

# 프록시 IP 목록
def getProxyList():
    with open('proxy_list.txt', 'r', encoding='utf-8') as file:
        proxies = [line.strip() for line in file]
    random.shuffle(proxies)
    return proxies