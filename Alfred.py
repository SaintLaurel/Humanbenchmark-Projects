import pyautogui
import time

def main():
    x, y = 200, 200
    blu = pyautogui.pixel(x, y)
    pyautogui.moveTo((x, y), duration=0.001)
    pyautogui.click()

    while True:
        click = pyautogui.pixel(x, y)

        if click == (30, 151, 80):
            pyautogui.click()
            time.sleep(0.1)
            pyautogui.click()

if __name__ == "__main__":
    main()

#suck cock Dima <3