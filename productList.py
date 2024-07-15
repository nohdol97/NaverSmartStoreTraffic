import random, time
from datetime import datetime

# 유입할 상품 목록
def getMidValueKeywordList():
    try:
        with open('product_list.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 빈 줄을 무시
        mid_value_keyword = lines
        random.shuffle(mid_value_keyword)  # 셔플
        return mid_value_keyword
    except:
        time.sleep(3)
        getMidValueKeywordList()

def decreaseNum(mid_value):
    try:
        with open('product_list.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 빈 줄을 무시

        updated_lines = []
        isUpdated = False

        for line in lines:
            parts = line.split(',')
            # 해당하는 mid_value 라인의 숫자를 하나 뺌
            if parts[0] == mid_value and int(parts[-1]) > 0:
                # 마지막 숫자에서 1을 뺌
                parts[-1] = str(int(parts[-1]) - 1)
                isUpdated = True
            updated_lines.append(','.join(parts))

        if isUpdated:
            # 파일에 다시 쓰기
            with open('product_list.txt', 'w', encoding='utf-8') as file:
                for updated_line in updated_lines:
                    file.write(updated_line + '\n')
    except:
        time.sleep(3)
        decreaseNum(mid_value)

def checkProductNum(midValueKeywordStr):
    parts = midValueKeywordStr.split(',')
    if parts[-1] == '0' or parts[-1] == '-1':
        return False
    return True

def checkFinish(startTime):
    try:
        now = datetime.now()
        midnight = startTime.replace(hour=23, minute=50, second=0, microsecond=0)
        if now > midnight:
            return True
        with open('product_list.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 빈 줄을 무시
        for line in lines:
            parts = line.split(',')
            if int(parts[-1]) > 0:
                return False
        return True 
    except:
        time.sleep(3)
        checkFinish(startTime)

def errorProduct(mid_value):
    try:
        with open('product_list.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 빈 줄을 무시

        updated_lines = []
        isUpdated = False

        for line in lines:
            parts = line.split(',')
            if parts[0] == mid_value:
                # 유입수를 -1로 만듦
                parts[-1] = "-1"
                isUpdated = True
            updated_lines.append(','.join(parts))

        if isUpdated:
            # 파일에 다시 쓰기
            with open('product_list.txt', 'w', encoding='utf-8') as file:
                for updated_line in updated_lines:
                    file.write(updated_line + '\n')
    except:
        time.sleep(3)
        errorProduct(mid_value)