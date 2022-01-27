import pyautogui, time, threading, sys, os, keyboard
import datetime
from const import *

def save(a, b):
    file = open("logs.txt", "a")
    file.write(str(a) + str(b) + "\n")
    file.close()

save(time.strftime("[%m-%d:%H:%M:%S]"), ("Bot starting in " + str(resolution) + " resolution mode"))

if resolution == 1:
    if drake == 1:
        drake_c="gdrake.png"
        drake_strt = "strtg.png"
    if drake == 2:
        drake_c="bdrake.png"
        drake_strt = "strtb.png"
    if drake == 3:
        drake_c="rdrake.png"
        drake_strt = "strtr.png"
    if drake == 4:
        drake_c="drake2.png"
        drake_strt = "strtsin.png"
    if drake == 5:
        drake_c="ldrake.png"
        drake_strt = "strtl.png"
    if drake == 6:
        drake_c="bonedrake.png"
        drake_strt = "strtbone.png"
else:
    if drake == 1:
        drake_c="gdrake_1.png"
        drake_strt = "strt_1_g.png"
    if drake == 2:
        drake_c="bdrake_1.png"
        drake_strt = "strt_1_b.png"
    if drake == 3:
        drake_c="rdrake_1.png"
        drake_strt = "strt_1_r.png"
    if drake == 4:
        drake_c="drake2_1.png"
        drake_strt = "strt_1_sin.png"
    if drake == 5:
        drake_c="ldrake_1.png"
        drake_strt = "strt_1_l.png"
    if drake == 6:
        drake_c="bonedrake_1.png"
        drake_strt = "strt_1_bone.png"

if resolution == 1:
    try:
        pyautogui.click("X.png")
    except:
        pass

    time.sleep(1)

    try:
        pyautogui.click("X2.png")
    except:
        pass
else:
    try:
        pyautogui.click("X_1.png")
    except:
        pass

    time.sleep(1)

    try:
        pyautogui.click("X_2.png")
    except:
        pass

time.sleep(1)
if botmode==1:
    if resolution == 1:
        try:
            save(time.strftime("[%m-%d:%H:%M:%S]"), "Starting wave")
            pyautogui.click("b.png")
        except:
            pass
    else:
        try:
            save(time.strftime("[%m-%d:%H:%M:%S]"), "Starting wave")
            pyautogui.click("B_1.png")
        except:
            pass
else:
    if resolution == 1:
        try:
            save(time.strftime("[%m-%d:%H:%M:%S]"), "Starting drake")
            pyautogui.click("drake.png")
        except:
            pass
        time.sleep(1)
        try:
            pyautogui.click(drake_c)
        except:
            pass
        time.sleep(1)
        try:
            pyautogui.click(drake_strt)
        except:
            pass
    else:
        try:
            save(time.strftime("[%m-%d:%H:%M:%S]"), "Starting drake")
            pyautogui.click("drake_1.png")
        except:
            pass
        time.sleep(1)
        try:
            pyautogui.click(drake_c)
        except:
            pass
        time.sleep(1)
        try:
            pyautogui.click(drake_strt)
        except:
            pass


def click_champs():
    if resolution == 1:
        try:
            pyautogui.click(x=463, y=160)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=576, y=156)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=465, y=287)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=578, y=281)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=684, y=284)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=458, y=419)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=567, y=419)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=683, y=424)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=230, y=601)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=231, y=759)
        except:
            pass
        e = datetime.datetime.now()
        save(time.strftime("[%m-%d:%H:%M:%S]"), "Click session done")
    else:
        try:
            pyautogui.click(x=335, y=120)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=411, y=120)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=339, y=215)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=412, y=207)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=485, y=213)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=336, y=304)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=412, y=298)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=481, y=300)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=174, y=422)
        except:
            pass
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=178, y=541)
        except:
            pass
        e = datetime.datetime.now()
        save(time.strftime("[%m-%d:%H:%M:%S]"), "Click session done")
    
def timer():
    time.sleep(wave_time)
    e = datetime.datetime.now()
    save(time.strftime("[%m-%d:%H:%M:%S]"), "Game ended restarting....")
    os.execl(sys.executable, sys.executable, *sys.argv)
        
thread = threading.Thread(target=timer)
thread.daemon = True
thread.start()

while True:
    click_champs()

    if keyboard.is_pressed("c"):
        save(time.strftime("[%m-%d:%H:%M:%S]"), "Script terminated by user")
        exit(1)
        
    if botmode==0:
        if resolution==1:
            try:
                pyautogui.click("get.png")
            except:
                pass
        else:
            try:
                pyautogui.click("get_1.png")
            except:
                pass



