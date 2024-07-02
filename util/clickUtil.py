import allElements

def clickNext(driver, i):
    next_button = allElements.getNextButton(driver, i)
    element_location = next_button.location['y']
    offset = -150  # 요소 위치에서 위로 스크롤할 픽셀 값
    driver.execute_script(f"window.scrollTo(0, {element_location + offset});")
    next_button.click()
    return True

def clickTarget(driver, elements):
    try:
        # 상품 클릭 시도
        # elements[0].click()
        driver.execute_script("arguments[0].setAttribute('target', '_self'); arguments[0].click();", elements)
    except Exception as e:
        # 가려져 있는 요소 찾기
        overlapping_element = driver.execute_script("""
            var elem = arguments[0];
            var rect = elem.getBoundingClientRect();
            return document.elementFromPoint(rect.left + rect.width / 2, rect.top + rect.height / 2);
        """, elements[0])
        
        # 가려져 있는 요소 클릭
        # driver.execute_script("arguments[0].click();", overlapping_element)
        driver.execute_script("arguments[0].setAttribute('target', '_self'); arguments[0].click();", overlapping_element)