import pyautogui, time, threading, sys, os, keyboard
from const import *

def save(a, b):
    file = open("logs.txt", "a")
    file.write(str(a) + str(b) + "\n")
    file.close()

save(time.strftime("[%m-%d:%H:%M:%S]"), ("Bot starting in " + str(resolution) + " resolution mode"))

if resolution == 1:
    if drake == 1:
        drake_c_x= 1227
        drake_c_y= 234
        drake_strtx = 1646
        drake_strty = 238
    if drake == 2:
        drake_c_x = 1227
        drake_c_y = 367
        drake_strtx = 1652
        drake_strty = 375
    if drake == 3:
        drake_c_x = 1224
        drake_c_y = 507
        drake_strtx = 1648
        drake_strty = 512
    if drake == 4:
        drake_c_x = 1218
        drake_c_y = 641
        drake_strtx = 1648
        drake_strty = 648
    if drake == 5:
        drake_c_x = 1232
        drake_c_y = 782
        drake_strtx = 1649
        drake_strty = 776
    if drake == 6:
        drake_c_x = 1232
        drake_c_y = 782
        drake_strtx = 1224
        drake_strty = 916
else:
    if drake == 1:
        drake_c_x = 855
        drake_c_y = 175
        drake_strtx = 1149
        drake_strty = 270
    if drake == 2:
        drake_c_x = 859
        drake_c_y = 266
        drake_strtx = 1159
        drake_strty = 916
    if drake == 3:
        drake_c_x = 859
        drake_c_y = 363
        drake_strtx = 1150
        drake_strty = 363
    if drake == 4:
        drake_c_x = 862
        drake_c_y = 455
        drake_strtx = 1143
        drake_strty = 455
        print(drake_c_x, drake_c_y, drake_strtx, drake_strty)
    if drake == 5:
        drake_c_x = 862
        drake_c_y = 545
        drake_strtx = 1157
        drake_strty = 544
    if drake == 6:
        drake_c_x = 862
        drake_c_y = 641
        drake_strtx = 1165
        drake_strty = 644

if resolution == 1:
    try:
        pyautogui.click(x=1438, y=276)
    except:
        pass

    time.sleep(1)

    try:
        pyautogui.click(x=1758, y=140)
    except:
        pass
else:
    try:
        pyautogui.click(x=1019, y=203)
    except:
        pass

    time.sleep(1)

    try:
        pyautogui.click(x=1230, y=101)
    except:
        pass

time.sleep(1)
if botmode==1:
    if resolution == 1:
        try:
            save(time.strftime("[%m-%d:%H:%M:%S]"), "Starting wave")
            pyautogui.click(x=1702, y =938)
        except:
            pass
    else:
        try:
            save(time.strftime("[%m-%d:%H:%M:%S]"), "Starting wave")
            pyautogui.click(x=1192, y=665)
        except:
            pass
else:
    if resolution == 1:
        try:
            save(time.strftime("[%m-%d:%H:%M:%S]"), "Starting drake")
            pyautogui.click(x=921, y=356)
        except:
            pass
        time.sleep(1)
        try:
            pyautogui.click(drake_c_x, drake_c_y)
        except:
            pass
        time.sleep(1)
        try:
            pyautogui.click(x=drake_strtx, y=drake_strty)
        except:
            pass
    else:
        try:
            save(time.strftime("[%m-%d:%H:%M:%S]"), "Starting drake")
            pyautogui.click(x=650, y=253)
        except:
            pass
        time.sleep(1)
        try:
            pyautogui.click(drake_c_x, drake_c_y)
        except:
            pass
        time.sleep(1)
        try:
            pyautogui.click(x=drake_strtx, y=drake_strty)
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
        time.sleep(cast_interval)
        try:
            pyautogui.click(x=463, y=555)
        except:
            pass
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
            pas
        save(time.strftime("[%m-%d:%H:%M:%S]"), "Click session done")
    
def timer():
    time.sleep(wave_time)
    if botmode == 0:
        if resolution == 1:
            if auto_delete_b_items == 1:
                try:
                    pyautogui.click("adios.png")
                except:
                    pass
                time.sleep(0.3)
                try:
                    pyautogui.click("adios.png")
                except:
                    pass
                time.sleep(1)
            else:
                try:
                    pyautogui.click(x=1099, y=769)
                except:
                    pass
        else:
            if auto_delete_b_items == 1:
                try:
                    pyautogui.click("adios_1.png")
                except:
                    pass
                time.sleep(0.3)
                try:
                    pyautogui.click("adios_1.png")
                except:
                    pass
            else:
                try:
                    pyautogui.click(x=778, y=560)
                except:
                    pass

    time.sleep(2)
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




