#pip install -r requirements.txt
import time
import keyboard
import pyautogui
from windows import moveTo




def find_search():
    search = pyautogui.locateCenterOnScreen("image/search.png", region=(0, 0, 200, 600), grayscale=True, confidence=0.70)
    # 110 540
    if search is not None and search.x in range(106,146) and search.y in range(504,544):
        
        print("Click summon")
        pyautogui.click(x = 230, y = 960)
        time.sleep(2)

        print("Click search")
        pyautogui.click(x = 340, y = 333)
        time.sleep(2)

        print("Click X")
        pyautogui.click(x = 510, y = 975)
        time.sleep(2)

        print("Click summon again")
        pyautogui.click(x = 230, y = 960)
        time.sleep(2)
   
def summon_gear():
    gear = pyautogui.locateCenterOnScreen("image/gear.png", region=(0, 0, 200, 600), grayscale=True, confidence=0.70)
 
    if gear is not None and gear.x in range(106,146) and gear.y in range(504,544):
        
        for i in range(3):

            print("Click summon gear")
            pyautogui.click(x = 280, y = 800)
            time.sleep(2)

            print("Click dismantle")
            pyautogui.click(x = 200, y = 820)
            time.sleep(2)
    
print("Run.......")
moveTo()
time.sleep(2)
while not keyboard.is_pressed('q'):
    # claim quest
    pyautogui.click(x = 125, y = 540)
    time.sleep(2)

    find_search()
    
    summon_gear()


   