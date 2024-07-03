import random, time

# 유입할 상품 목록
def getMidValueKeywordList():
    try:
        with open('product_list.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]
        mid_value_keyword = lines[1:]  # 첫 줄 제외
        random.shuffle(mid_value_keyword)  # 셔플
        return mid_value_keyword
    except:
        time.sleep(3)
        getMidValueKeywordList()

def decreaseNum():
    try:
        with open('product_list.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]

        # 헤더를 포함한 모든 줄을 처리
        updated_lines = [lines[0]]  # 첫 줄(헤더)은 그대로 추가

        for line in lines[1:]:
            parts = line.split(',')
            if len(parts) == 3:
                # 마지막 숫자에서 1을 뺌
                try:
                    parts[-1] = str(int(parts[-1]) - 1)
                    updated_lines.append(','.join(parts))
                except ValueError:
                    print(f"Error parsing number from line: {line}")

        # 파일에 다시 쓰기
        with open('product_list.txt', 'w', encoding='utf-8') as file:
            for updated_line in updated_lines:
                file.write(updated_line + '\n')
    except:
        time.sleep(3)
        decreaseNum()

def checkNegative(midValueKeywordStr):
    parts = midValueKeywordStr.split(',')
    if int(parts[-1]) < 0:
        return False
    return True

def checkFinish():
    try:
        all_below_zero = True
        with open('product_list.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]

        for line in lines[1:]:
            parts = line.split(',')
            if int(parts[-1]) > 0:
                all_below_zero = False
        return all_below_zero
    except:
        time.sleep(3)
        checkFinish()