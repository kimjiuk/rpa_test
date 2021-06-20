import pyautogui

#마우스 이동
#pyautogui.moveTo(200,100) # 지정한 위치로 마우스 이동
#pyautogui.moveTo(100,200,duration=5)#5초 동안 이동
#pyautogui.moveTo(100,200,duration=1)
#pyautogui.moveTo(200,200,duration=1)
#pyautogui.moveTo(300,200,duration=1)

#상대좌표로 마우스 이동(현재 커서가 있는 위치로부터)
pyautogui.moveTo(100,100, duration=0.25)
print(pyautogui.position()) #마우스커서 움직임의 정보 point(x,y)
pyautogui.move(100,100,duration=1)
print(pyautogui.position()) #마우스커서 움직임의 정보 point(x,y)
p=pyautogui.position()
print(p[0],p[1])