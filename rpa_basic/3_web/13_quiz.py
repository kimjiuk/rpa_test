#quiz) selenium 을 이용하여 아래 업무를 자동으로 수행하는 프로그램을 작성하시오.

# 1. http://www.w3schools.com 접속 
# 2. 화면 중간 learn html 클릭
# 3. 상단 메뉴 중 how to 클릭
# 4. 죄측 메뉴 중 contact from 메뉴 클릭
# 5. 입력란에 아래 값 입력
    #first name : 나도
    #last name : 코딩
    #country : canada
    #subject : 퀴즈 완료하였습니다.
    # 위 값들은 변수로 미리 저장해주세요
# 6. 5초 대기 후 submit 버튼 클릭
# 7. 5초 대기 후 브라우저 종료
from selenium import webdriver
import time
#1
browser = webdriver.Chrome()
browser.get('http://www.w3schools.com')
browser.maximize_window()
#2
elem = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/a[1]').click()
#3
elem = browser.find_element_by_xpath('//*[@id="right"]/div[6]/div[1]/h4/a').click()
time.sleep(1)
#4
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click()
#보다 정확하게 할려면~
#elem = browser.find_element_by_link_text('Contact Form').click()
#elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]') #가장 좋은 방법 - 링크가 2개일수도있으니까..
#elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click()
#5
time.sleep(1)
browser.find_element_by_xpath('//*[@id="fname"]').send_keys('나도')
browser.find_element_by_xpath('//*[@id="lname"]').send_keys('코딩')
browser.find_element_by_xpath('//*[@id="country"]/option[2]').click()
#browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format"(country)).click()

browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys('퀴즈 완료하셨습니다..')

time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()