# 셀레니움
# 웹페이지 텍스트 프레임 자동화 도구.
# 웹페이지를 이용하는데 아주중요하다고함.

from selenium import webdriver

#browser = webdriver.Chrome("./chromedriver.exe")
browser = webdriver.Chrome()



#하... 너무 어렵..

# 정리
# 네이버 이동
browser.get('http://naver.com')

# 카페 메뉴 찾기 
elem = browser.find_element_by_link_text('카페')

# 속성 가져오기
elem.get_attribute('href')
elem.get_attribute('class')

# 클릭
browser.click()

# 뒤로 가기
browser.back()

# 앞으로 가기
browser.forward()

# 새로고침
browser.refresh()

# 검색창 찾기
elem = browser.find_element_by_id('query')

# 글자 입력하기
elem.send_keys('나도 코딩')

# enter 치기
from selenium.webdriver.common.keys import Keys
elem.send_keys(Keys.ENTER)
elem.get_attribute('href')

# a 태그 찾기
elem = browser.find_element_by_tag_name('a')
elem.get_attribute('href')

# a 태그 모두 찾기
elems = browser.find_elements_by_tag_name('a')
for e in elems:
    e.get_attribute('href')

# 다음으로 이동
browser.get('http://daum.net')

# 검색창 찾기
elem = browser.find_element_by_name('q')

# 글자 입력하기
elem.send_keys("나도 코딩")

# 글자 지우기
elem.clear()

# 글자 입력하기
elem.send_keys("나도 코딩")

# 검색 버튼 찾기
elem = browser.find_element_by_xpath('찾은거 넣기')

# 클릭하기
elem.click()

# 스크린샷 찍기
browser.save_screenshot('daum.png')

# 페이지 소스 보기
browser.pahge_source

# 브라우저 종료
browser.close() #현재탭닫기
browser.quit()  # 브라우저 종료하기

