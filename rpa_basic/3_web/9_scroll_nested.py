from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(2)

# 특정영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')

# actionchain

from selenium.webdriver.common.action_chains import ActionChains
# 방법 1 : actionchain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 방법 2 : 좌표정보이용
xy = elem.location_once_scrolled_into_view
print("type:", type(xy)) #dict
print("value:", xy)
time.sleep(2)
browser.quit()