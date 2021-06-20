import time
from selenium import webdriver
# 안될때 sleep을 통해 브라우저 입력을 기다리자!
browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://shopping.naver.com/home/p/index.nhn')

# 무선마우스입력
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys('무선 마우스')
time.sleep(2)
# 검색버튼 클릭
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

# enter 방법
#elem = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys('무선 마우스')
#from selenium.webdriver.common.keys import Keys
#elem.send_keys('무선마우스')
#elem.send_keys(Keys.ENTER) # 검색 버튼 클릭을 위해 enter 처리


# 스크롤
# 지정한 위치로 스크롤 내리기
#browser.execute_script('window.scrollTo(0,1080)') # 1920 * 1080(모니터 해상도)
#browser.execute_script('window.scrollTo(0,2080)') # 1920 * 1080(모니터 해상도)

# 화면 가장 아래로 스크롤 내리기
#browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')





# 동적 페이지에 대해서 마지막까지 스크롤 반복 수행
interval = 2 # 2초에 한번씩 스크롤 내리기
# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복수행
while True:
    # 스크롤을 화면 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height : # 직전 높이와 같은면 , 즉 높이 변화가 없으면
        break # 반복문 탈출

    prev_height = curr_height

# 맨 위로 올리기
browser.execute_script('window.scrollTo(0,0)')
time.sleep(3)
browser.quit()