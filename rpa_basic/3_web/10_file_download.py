from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs',{'download.default_directory':r'C:\Users\wldnr\OneDrive\바탕 화면\workspace'})


browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')
browser.maximize_window()
browser.switch_to.frame('iframeResult')

#다운로드 링크 클릭
elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()


time.sleep(2)
browser.quit()