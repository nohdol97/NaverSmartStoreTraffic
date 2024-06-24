import allElements

def clickNext(driver, i):
    next_button = allElements.getNextButton(driver, i)
    element_location = next_button.location['y']
    offset = -150  # 요소 위치에서 위로 스크롤할 픽셀 값
    driver.execute_script(f"window.scrollTo(0, {element_location + offset});")
    next_button.click()
    return True