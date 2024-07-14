import pyautogui
import pyperclip
import time

def select_and_copy_text():
    pyautogui.click(1346, 1045)
    time.sleep(0.5) 

    time.sleep(5)
    pyautogui.moveTo( 606 ,  257)
    pyautogui.dragTo(1852 , 890 , duration=1) 
    time.sleep(0.5)

  
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5) 

    copied_text = pyperclip.paste()
    pyautogui.click( 812 , 546)

    pyautogui.click(1290  ,1049)
    time.sleep(0.5) 

    pyautogui.click(736 , 941)
    time.sleep(0.5)
     
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5) 

    pyautogui.click(1407 , 942)
    time.sleep(20)

    pyautogui.click(961 , 862)
    time.sleep(2)

    pyautogui.click(586 , 803)
    time.sleep(0.5)

    answered_text= pyperclip.paste()

    pyautogui.click(1346, 1045)
    time.sleep(0.5)

    pyautogui.click(880  , 967)
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5) 

    pyautogui.click(1849 , 955)
    time.sleep(0.5)

    return answered_text

answered_text = select_and_copy_text()
print(f"answered  text: /n {answered_text}")

