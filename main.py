import time
import work
import timeValues as timeValues
import traceback
import productList
import driverInfo

driver = driverInfo.create_driver()
for midValueKeywordStr in productList.getMidValueKeywordList():
    try:
        work.mobileNaverShopping(driver, midValueKeywordStr)
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
    time.sleep(timeValues.getWaitLoadingTime())