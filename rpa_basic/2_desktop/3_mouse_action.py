import pyautogui
#pyautogui.sleep(3) #3초대기
#print(pyautogui.position())#현재 마우스 위치
#pyautogui.click(64,17,duration=1) #64,17 좌표 클릭

#click=mouseDown()+mouseUp() 합친상태
#mousedown은 마우스누른상태, mouseup은 누른걸 뗀상태
#드래그앤드랍방식일때 씀
#pyautogui.doubleClick()#더블클릭
#pyautogui.click(clicks=500)
#pyautogui.rightClick() #오른쪽클릭
#pyautogui.middleClick()
#pyautogui.drag(100,0)//상대좌표
#pyautogui.dragTo()//절대좌표
pyautogui.scroll(-300) # 위 방향으로 300만큼 스크롤.
#양수이면 위,음수이면 아래 방향으로 스크롤
