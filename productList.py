import random

# 유입할 상품 목록
def getMidValueKeywordList():
    with open('product_list.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    mid_value_keyword = lines[1:]  # 첫 줄 제외
    random.shuffle(mid_value_keyword)  # 셔플
    return mid_value_keyword