import pyautogui

pyautogui.PAUSE = 2

#抛竿-上钩检测-收回

run=False
s=0 #0为初抛 1为抛竿 2为上钩收杆

def auto_fish():
    global s
    #print("a")
    if s==0:
        pyautogui.press("Esc")
        pyautogui.click(button="right")
        s=1
    elif s==2:
        pyautogui.click(button="right")
        s=1
    elif pyautogui.locateOnScreen('fish.png',confidence=0.9):
        pyautogui.click(button="right")
        s=2

while True:
    #是否开启自动钓鱼 #start #stop
    try:
        if pyautogui.locateOnScreen('start.png',confidence=0.9):
            run=True
            print("start")
    except:
        pass
    while run:
        try:
            try:
                if pyautogui.locateOnScreen('stop.png',confidence=0.9):
                    run=False
                    s=0
                    pyautogui.press("Esc")
                    print("stop")
            except:
                auto_fish()
        except:
            pass
