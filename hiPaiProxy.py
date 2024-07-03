import random
import time
from datetime import datetime, timedelta

def getProxyIp(ID):
    for i in range(10):
        try:
            with open('hiPaiIp.txt', 'r') as file:
                lines = file.readlines()

            # 빈 줄 제거 및 각 줄에서 ','로 구분
            lines = [line.strip() for line in lines if line.strip()]

            # lines 중 첫번째 줄 선택
            selected_line = lines.pop(0)

            # 선택된 줄 hiPaiIp.txt 에서 제거
            try:
                with open('hiPaiIp.txt', 'w') as file:
                    for line in lines:
                        file.write(line + '\n')
            except Exception as e:
                print(f"Error writing file: {e}")
                time.sleep(3)
                getProxyIp(ID)

            return selected_line
        except Exception as e:
            print(f"Error reading file: {e}")
            time.sleep(3)
            pass
    
def setProxyIp(hiPaiProxy):
    for i in range(10):
        try:
            with open('hiPaiIp.txt', 'a') as file:
                file.write(hiPaiProxy + '\n')
        except Exception as e:
            print(f"Error editing file: {e}")
            time.sleep(3)
            pass