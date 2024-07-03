import random
import time
from datetime import datetime, timedelta

def getProxyIp(ID):
    try:
        with open('hiPaiIp.txt', 'r') as file:
            lines = file.readlines()
    except:
        time.sleep(3)
        getProxyIp(ID)

    # 빈 줄 제거 및 각 줄에서 ','로 구분
    lines = [line.strip() for line in lines if line.strip()]

    # lines 중 첫번째 줄 선택
    selected_line = lines.pop(0)

    # 선택된 줄 hiPaiIp.txt 에서 제거
    try:
        with open('hiPaiIp.txt', 'w') as file:
            for line in lines:
                file.write(line + '\n')
    except:
        time.sleep(3)
        getProxyIp(ID)

    return selected_line

def setProxyIp(hiPaiProxy):
    try:
        with open('hiPaiIp.txt', 'a') as file:
            file.write(hiPaiProxy + '\n')
    except:
        time.sleep(3)
        setProxyIp(hiPaiProxy)