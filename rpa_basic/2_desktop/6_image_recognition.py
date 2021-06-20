import pyautogui
#file_menu = pyautogui.locateOnScreen("file_menu.png")
#print(file_menu)
#pyautogui.click(file_menu)

#trash_icon = pyautogui.locateOnScreen("trash_icon.png")
#print (trash_icon)
#pyautogui.click(trash_icon)

#screen = pyautogui.locateOnScreen("screenshot.png")
#print(screen)

#for i in pyautogui.locateAllOnScreen("checkbox.png"):
#    print(i)
#    pyautogui.click(i, duration = 1)


#속도개선
# 1. GrayScale
#trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale = True)
#pyautogui.moveTo(trash_icon)
#속도는 조금 빨라지나 정확도는 조금 떨어진다!

#2. 범위지정
#trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(x, y, width, height))
#pyautogui.moveTo(trash_icon)
#pyautogui.mouseInfo()
#1720,628 30,30,30 #1E1E1E
#1764,799 30,30,30 #1E1E1E
#trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1720, 628, 100, 200))
#pyautogui.moveTo(trash_icon)

#3. 정확도 지정
#run_btn = pyautogui.locateOnScreen("run_btn.png", confidence = 0.9)#90퍼
#pyautogui.moveTo(run_btn)

#자동화 대상이 바로 보여지지 않는 경우

#file_menu = pyautogui.locateOnScreen("file_menu.png")
#if file_menu:
#    pyautogui.click(file_menu)
#else:
#    print("no")

#while file_menu is None:
#    file_menu = pyautogui.locateOnScreen("file_menu.png")
#    print("no")
#pyautogui.click(file_menu)

#2. 일정 시간동안 기다리기(timeout)

import time
import sys

#timeout = 10 #10초대기
#start = time.time()#시작시간설정
#file_menu = None
#while file_menu is None:
#    file_menu = pyautogui.locateOnScreen("file_menu.png")
#    end = time.time()# 종료시간설정
#    if end - start > timeout: #지정한 10초를 초과하면
#        print("시간종료")
#        sys.exit()

#pyautogui.click(file_menu)

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end-start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). terminate program")
        sys.exit()

    
my_click("file_menu.png",1)
