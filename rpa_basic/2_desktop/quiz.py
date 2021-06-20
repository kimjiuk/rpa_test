#quiz 아래 동작을 자동으로 수행하는 프로그램을 작성하시오
# 1. 그림판 실행 (단축키 : win+r, 입력값 : mspaint) 및 최대화

# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
 # - 입력 글자 : "참 잘했어요"
# 3. 5초 대기 후 그림판 종료
 # 이때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함.
import pyperclip
import pyautogui
import sys
pyautogui.hotkey("win","r")
pyautogui.write(["m","s","p","a","i","n","t","enter"],interval=0.1) 
#pyautogui.press("enter")
pyautogui.sleep(2)

w = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
if w.isMaximized == False:
    w.maximize()
menu = pyautogui.locateOnScreen("A.png", confidence=0.8)
if menu:
    print(menu)
    pyautogui.click(menu, interval=0.1)
else :
    print("no")
    sys.exit()
#765,370 255,255,255 #FFFFFF

pyautogui.moveTo(765,370, duration=2)

pyautogui.click(clicks=1)
pyperclip.copy("참 잘했어요") 
pyautogui.hotkey("ctrl","v") 
pyautogui.sleep(5)
pyautogui.hotkey("alt","F4")
pyautogui.sleep(2)
pyautogui.hotkey("alt","n")
