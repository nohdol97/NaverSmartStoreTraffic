import random, time
from datetime import datetime

import setValues

# 유입할 상품 목록
def getMidValueKeywordList():
    try:
        with open('product_list.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 빈 줄을 무시

        if not lines:
            return 0, []
        
        # 맨 마지막 줄을 total로 분리
        total = lines.pop() if lines else None

        # 가장 앞의 숫자를 추출하여 정수 리스트로 변환
        first_numbers = [int(line.split(',')[0]) for line in lines]

        # 가장 큰 숫자를 찾음
        max_number = max(first_numbers)

        # 가장 큰 숫자와 일치하는 모든 줄을 필터링
        mid_value_keyword = [line for line in lines if int(line.split(',')[0]) == max_number]

        updated_lines = []
        isUpdated = False

        for line in mid_value_keyword:
            parts = line.split(',')
            if int(parts[0]) > 0:
                parts[0] = str(int(parts[0]) - 1)
            # 가장 앞에가 0이 되면 두번째 것을 복사
            if int(parts[0]) == 0:
                parts[0] = str(int(parts[1]) * setValues.windowCount)
            updated_lines.append(','.join(parts))
            isUpdated = True

        if isUpdated:
            # 파일에 다시 쓰기
            with open('product_list.txt', 'w', encoding='utf-8') as file:
                for updated_line in updated_lines:
                    file.write(updated_line + '\n')
                if total:
                    file.write(total + '\n')  # 마지막 줄 다시 쓰기

        random.shuffle(updated_lines)  # 셔플
        return total, updated_lines
    except:
        time.sleep(3)
        getMidValueKeywordList()

def decreaseNum(mid_value):
    try:
        with open('product_list.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 빈 줄을 무시

        updated_lines = []
        isUpdated = False

        # 맨 마지막 줄을 total로 분리
        total = lines.pop() if lines else None

        for line in lines:
            parts = line.split(',')
            # 해당하는 mid_value 라인의 숫자들을 하나씩 뺌
            if parts[2] == mid_value:
                if int(parts[-1]) > 0:
                    parts[-1] = str(int(parts[-1]) - 1)
                isUpdated = True
            updated_lines.append(','.join(parts))

        if isUpdated:
            # 파일에 다시 쓰기
            with open('product_list.txt', 'w', encoding='utf-8') as file:
                for updated_line in updated_lines:
                    file.write(updated_line + '\n')   
                if total:
                    file.write(total + '\n')  # 마지막 줄 다시 쓰기     
    except:
        time.sleep(3)
        decreaseNum(mid_value)

def checkProductNum(midValueKeywordStr):
    parts = midValueKeywordStr.split(',')
    if parts[-1] == '0' or parts[-1] == '-1':
        return False
    return True

def checkFinish(startTime, id):
    try:
        now = datetime.now()
        midnight = startTime.replace(hour=23, minute=50, second=0, microsecond=0)
        if now > midnight:
            return True
        if not id:
            with open('product_list.txt', 'r', encoding='utf-8') as file:
                lines = [line.strip() for line in file if line.strip()]  # 빈 줄을 무시
                for line in lines:
                    parts = line.split(',')
                    if int(parts[-1]) > 0:
                        return False
        else:
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