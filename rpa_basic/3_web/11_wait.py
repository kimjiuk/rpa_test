# 웹 브라우저가 로딩중일때
# 1. 방법 : time.sleep(10) 
# - 본인이 시간 지정

# 2. 방법 : 로딩이 끝나고 블라우저 탐색

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 첫번째 엘레멘트가 나올때까지
try: 
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,'내가 원하는 엑스패스')))
    print(elem.text)
except:
    print("실패요")