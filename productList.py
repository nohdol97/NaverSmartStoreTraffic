import random, time, os
from datetime import datetime, timedelta

# 유입할 상품 목록
def getMidValueKeywordList():
    try:
        with open('product_list.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]
        mid_value_keyword = lines
        random.shuffle(mid_value_keyword)  # 셔플
        return mid_value_keyword
    except:
        time.sleep(3)
        getMidValueKeywordList()

def decreaseNum(mid_value):
    try:
        with open('product_list.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]

        updated_lines = []

        for line in lines:
            parts = line.split(',')
            # 해당하는 mid_value 라인의 숫자를 하나 뺌
            if parts[0] == mid_value and int(parts[-1]) > 0:
                # 마지막 숫자에서 1을 뺌
                parts[-1] = str(int(parts[-1]) - 1)
            updated_lines.append(','.join(parts))

        # 파일에 다시 쓰기
        with open('product_list.txt', 'w', encoding='utf-8') as file:
            for updated_line in updated_lines:
                file.write(updated_line + '\n')
    except:
        time.sleep(3)
        decreaseNum()

def checkProductNum(midValueKeywordStr):
    parts = midValueKeywordStr.split(',')
    if int(parts[-1]) == 0:
        return False
    return True

def checkFinish():
    try:
        if os.path.exists("hiPaiIp.txt"):
            with open('product_list.txt', 'r', encoding='utf-8') as file:
                lines = [line.strip() for line in file]
            for line in lines:
                parts = line.split(',')
                if int(parts[-1]) > 0:
                    return
        
        # 끝났다면 다음날 까지 대기, main 에서 23시 55분에 다시 채워줌
        now = datetime.now()
        print(f"finish time: {now}")
        next_midnight = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        sleep_time = (next_midnight - now).total_seconds()
        time.sleep(sleep_time)
    except:
        time.sleep(3)
        checkFinish()