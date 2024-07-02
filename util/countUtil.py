import allElements

def getCountAll(driver):
    for i in range(4, 10):
        elements = allElements.getAllProduct(driver, i)
        if elements:
            break
    
    return len(elements)

def getFindCountByMidValue(driver, mid_value):
    target_id = f'_sr_lst_{mid_value}'
    for i in range(4, 10):
        elements = allElements.getAllProduct(driver, i)
        if elements:
            break

    count = 0
    for element in elements:
        count += 1
        if element.get_attribute('id') == target_id:
            break
    return count