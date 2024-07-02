import random
import time
from datetime import datetime, timedelta

def getProxyIp(ID):
    with open('hiPaiIp.txt', 'r') as file:
        lines = file.readlines()
    
    # 빈 줄 제거 및 각 줄에서 ','로 구분
    lines = [line.strip() for line in lines if line.strip()]

    valid_lines = []
    for line in lines:
        parts = line.split(',')
        if len(parts) > 1 and ':' in parts[0]:
            try:
                # 시간 부분 확인
                timestamp = datetime.strptime(parts[-1], '%Y-%m-%d %H:%M:%S')
                # 한 시간 차이나면 로그인 가능하게 변경
                if datetime.now() - timestamp > timedelta(hours=1):
                    # 시간 부분 제거해서 추가
                    valid_lines.append(','.join(parts[:-1]))
            except ValueError:
                pass
        # IP 만 있다면, 추가
        elif len(parts) == 1:
            valid_lines.append(line)
    
    # valid_lines가 비어있지 않고, 로그인 한 경우 랜덤한 한 줄 선택
    if valid_lines and ID:
        random_line = random.choice(valid_lines)
        
        with open('hiPaiIp.txt', 'w') as file:
            for line in lines:
                if line == random_line or line == random_line + ',' + parts[-1]:
                    file.write(f'{ID},{random_line},{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
                else:
                    # 나머지 줄 그대로 남김
                    file.write(line + '\n')
        return random_line, True
    else:
        time.sleep(random.uniform(300, 600))
        # 아무 IP 사용, 로그인 하지 않음
        random_line = random.choice(lines)
        return random_line[0], False

def eraseID(ID):
    with open('hiPaiIp.txt', 'r') as file:
        lines = file.readlines()
    
    with open('hiPaiIp.txt', 'w') as file:
        for line in lines:
            parts = line.split(',')
            if parts[0] == ID:
                # ID 부분을 제거한 나머지 부분을 다시 작성
                file.write(','.join(parts[1:]) + '\n')
            else:
                file.write(line)