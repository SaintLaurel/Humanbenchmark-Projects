import pyautogui
import time

def main():
    x, y = 200, 200
    pyautogui.moveTo(x, y)
    pyautogui.click()

    counter = 0

    while True:
        colour = pyautogui.pixel(x, y)

        if colour == (30, 151, 80):
            pyautogui.click()
            time.sleep(0.1)
            pyautogui.click()

            counter += 1
            if counter == 5:
                break

if __name__ == "__main__":
    main()

# suck cock Dima <3