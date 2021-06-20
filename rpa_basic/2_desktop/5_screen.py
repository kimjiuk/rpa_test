import pyautogui
#스크린 샷 찍기
#img = pyautogui.screenshot()
#img.save("screenshot.png")#파일로저장

#pyautogui.mouseInfo()

#838,131 204,0,0 #CC0000
#1221,777 37,37,38 #252526

pixel = pyautogui.pixel(1221,777)
print(pixel)

print(pyautogui.pixelMatchesColor(1221,77,(37,37,38)))

