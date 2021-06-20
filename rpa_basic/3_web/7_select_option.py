#https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select')

browser.switch_to.frame('iframeResult')
# index를 찾아 클릭하는 방법
#//*[@id="cars"]/option[3]
#elem = browser.find_element_by_xpath('//*[@id="cars"]/option[3]')
#elem.click()

# 텍스트 값을 통해서 선택하는 방법
# 옵션 중에서 텍스트가 아우디인 항목 선택
#elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')

# 텍스트 값이 부분 일치하는 항목 선택하는 방법.
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()
time.sleep(2)
browser.quit()
