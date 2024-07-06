import allElements
import time

def clickNext(driver, i):
    next_button = allElements.getNextButton(driver, i)
    element_location = next_button.location['y']
    offset = -150  # 요소 위치에서 위로 스크롤할 픽셀 값
    driver.execute_script(f"window.scrollTo(0, {element_location + offset});")
    next_button.click()
    return True

def clickTarget(driver, element):
    try:
        # 요소를 현재 탭에서 열리도록 설정하고 클릭
        driver.execute_script("""
            arguments[0].setAttribute('target', '_self');
            arguments[0].setAttribute('rel', 'noopener noreferrer');
        """, element)

        # 요소의 클릭 이벤트를 강제로 트리거
        driver.execute_script("arguments[0].click();", element)
        return True
    except Exception as e:
        print(f"Error clicking element: {e}")
        try:
            # 가려져 있는 요소 찾기
            overlapping_element = driver.execute_script("""
                var elem = arguments[0];
                var rect = elem.getBoundingClientRect();
                return document.elementFromPoint(rect.left + rect.width / 2, rect.top + rect.height / 2);
            """, element)
            
             # 가려져 있는 요소의 target 속성과 rel 속성을 변경하여 현재 탭에서 열리도록 설정
            driver.execute_script("""
                arguments[0].setAttribute('target', '_self');
                arguments[0].setAttribute('rel', 'noopener noreferrer');
            """, overlapping_element)
            
            # 가려져 있는 요소의 클릭 이벤트를 강제로 트리거
            driver.execute_script("arguments[0].click();", overlapping_element)
            return True
        except Exception as inner_e:
            print(f"Error clicking overlapping element: {inner_e}")
            return False
