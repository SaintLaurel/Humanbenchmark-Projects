import pyautogui
import keyboard
import win32api
import win32con
import time


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def main():
    while keyboard.is_pressed('q') == False:
        pic = pyautogui.screenshot(region=(0, 135, 943, 540))
        width, height = pic.size

        for x in range(0, width, 5):
            for y in range(0, height, 5):
                r, g, b = pic.getpixel((x, y))

                if b == 54:
                    click(x + 0, y + 135)
                    time.sleep(0.001)
                    break

if __name__ == "__main__":
    main()  