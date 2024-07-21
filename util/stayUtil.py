import util.randomUtil as randomUtil
import util.scrollUtil as scrollUtil
import timeValues as timeValues
import setValues

import time, random

def stay_target(driver):
    try:
        scrollUtil.scrollToEnd(driver, timeValues.getWaitInTargetTime())
        # randomValue = randomUtil.get_random_value()
        # if randomValue < 0.3: # 30퍼 확률
        #     scrollUtil.scrollToEnd(driver, timeValues.getWaitInTargetTime())
        # else:
        #     scrollUtil.scrollDetailPage(driver, timeValues.getWaitInTargetWithDetailTime())
    except:
        time.sleep(10)

def stay_more_time(driver):
    try:
        for i in range(random.randint(5, 15)):
            randomValue = randomUtil.get_random_value()
            if randomValue < 0.6:
                scrollUtil.scrollUp(driver)
            else:
                scrollUtil.scrollDown(driver)
            time.sleep(random.uniform(1, 2))
    except:
        pass