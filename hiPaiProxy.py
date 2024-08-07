import time

def getProxyIp():
    for i in range(10):
        try:
            with open('hiPaiIp.txt', 'r') as file:
                lines = file.readlines()

            # 빈 줄 제거
            lines = [line.strip() for line in lines if line.strip()]

            # lines 중 첫번째 줄 선택
            selected_line = lines.pop(0)
        
            # 선택된 줄 hiPaiIp.txt 에서 제거
            with open('hiPaiIp.txt', 'w') as file:
                for line in lines:
                    file.write(line + '\n')

            return selected_line
        except Exception as e:
            print(f"Error reading file: {e}")
            time.sleep(3)
            pass
    
def addProxyIp(hiPaiProxy):
    for i in range(10):
        try:
            with open('hiPaiIp.txt', 'a') as file:
                file.write(hiPaiProxy + '\n')
            break
        except Exception as e:
            print(f"Error editing file: {e}")
            time.sleep(3)
            pass