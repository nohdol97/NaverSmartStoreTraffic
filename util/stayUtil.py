import util.randomUtil as randomUtil
import util.scrollUtil as scrollUtil
import timeValues as timeValues

def stay_target(driver):
    randomValue = randomUtil.get_random_value()
    if randomValue < 0.3: # 30퍼 확률
        scrollUtil.scrollToEnd(driver, timeValues.getWaitInTargetTime())
    else:
        scrollUtil.scrollDetailPage(driver, timeValues.getWaitInTargetWithDetailTime())