import pyautogui

#fw = pyautogui.getActiveWindow() #현재 활성화된 창 vscode
#print(fw.title) #창의제목정보
#print(fw.size) #창의크기정보(가로ㅡ세로)
#print(fw.left, fw.top, fw.right, fw.bottom) #창의 좌표정보

#for w in pyautogui.getAllWindows():
#    print(w) #모든 윈도우 가져오기

#for w in pyautogui.getWindowsWithTitle("제목 없음"):
#    print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False : #현재 활성화가 되지 않았다면
    w.activate() #활성화(맨앞으로가져오기)

if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    w.maximize() #최대화
#if w.isMinimized == False: # 현재 최소화가 되지 않았다면
#    w.minimize() #최소화

w.restore() #화면 원복

w.close() #윈도우 닫기
