import pyautogui 
w = pyautogui.getWindowsWithTitle("제목 없음")[0] #메모장 1개 띄운 상태에서 가져옴
w.activate()

pyautogui.write("12345")

#pyautogui.write("i major computer enj", interval = 0.5)
#pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"],interval=0.25)
# test 순서대로 적고 왼쪽 방향키 2번 오른쪽 방향키2번 l a 순서대로 적고 enter 입력

#특수문자 -- shift+4 ->$
#pyautogui.keyDown("shift")#shift키를 누른 상태에서
#pyautogui.press("4") #숫자 4를 입력하고
#pyautogui.keyUp("shift") #shift키를 뗀다.


# 조합키
#pyautogui.keyDown("ctrl")
#pyautogui.keyDown("a")
#pyautogui.keyUp("a")
#pyautogui.keyUp("ctrl")
#복사나 구현하기 가능

#간편한 조합키
#pyautogui.hotkey("ctrl","alt","shift","a")
# ctrl 누르고 alt 누르고 shift 누르고 a 누르고 a 떼고 shift 떼고 ...

import pyperclip

#pyperclip.copy("나도코딩") #"나도코딩"글자를 클립보드에 저장
#pyautogui.hotkey("ctrl","v") #클립보드에 있는 내용을 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("나도코딩")


#자동화 프로그램 종료
#win : ctrl + alt + del
#mac : cmd + shift + option +q
