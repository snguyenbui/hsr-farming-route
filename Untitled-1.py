import time

import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import vgamepad as vg

gameWindow = gw.getWindowsWithTitle("Honkai: Star Rail")[0]
gameWindow.activate()

gamepad = vg.VX360Gamepad()

INPUT_BUFFER = 0.2
LOAD_TIME = 2.7

LEFT = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
RIGHT = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
UP = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
DOWN = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
A = vg.XUSB_BUTTON.XUSB_GAMEPAD_A
B = vg.XUSB_BUTTON.XUSB_GAMEPAD_B
X = vg.XUSB_BUTTON.XUSB_GAMEPAD_X
MAP = vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK
SPRINT = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER


def press(button):
    gamepad.press_button(button=button)
    gamepad.update()
    time.sleep(INPUT_BUFFER)
    gamepad.release_button(button=button)
    gamepad.update()
    time.sleep(INPUT_BUFFER)


def move(x, y, duration):
    gamepad.left_joystick(x_value=x, y_value=y)  # values between -32768 and 32767
    gamepad.update()
    time.sleep(duration)
    gamepad.left_joystick(x_value=0, y_value=0)
    gamepad.update()
    time.sleep(INPUT_BUFFER)


def resetLeftStick():
    gamepad.left_joystick(x_value=0, y_value=0)
    gamepad.update()
    time.sleep(INPUT_BUFFER)


def combat():
    while True:
        screenshot = pyautogui.screenshot(
            region=(
                gameWindow.top,
                gameWindow.left,
                gameWindow.width * 0.1,
                gameWindow.height * 0.15,
            )
        )
        screenshot = np.array(screenshot)

        cv2.imshow("title", screenshot)

        menu = pyautogui.locateOnScreen("menu.png", confidence=0.85)

        if cv2.pollKey() != -1 or menu:
            cv2.destroyAllWindows()
            break
    time.sleep(LOAD_TIME)


def spaceStation():
    press(MAP)
    time.sleep(LOAD_TIME)
    press(X)
    move(-32767, 0, 0.35)
    press(A)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(5500, 32767, 0.55)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 3.8)
    press(X)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(-32767, 0, 0.4)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 6.1)
    press(X)
    combat()

    move(32767, 0, 4.0)
    move(7000, -32767, 6.0)
    move(32767, 4000, 2.8)
    move(-6000, 32767, 6.0)
    press(X)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(5200, 0, 0.1)
    press(A)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 1.0)
    press(X)
    combat()

    move(-5000, 32767, 6.3)
    move(-32767, 0, 2.1)
    press(X)
    combat()

    move(32767, -17000, 3.0)
    move(32767, 20000, 2.0)
    move(32767, 32767, 2.0)
    move(6000, 32767, 5.2)
    move(-32767, 16000, 1.5)
    move(0, 32767, 1.9)
    move(32767, -18000, 0.5)
    press(X)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(6500, 6500, 0.5)
    press(A)
    press(A)
    press(A)
    time.sleep(LOAD_TIME)
    move(9000, -32767, 3.0)
    press(X)
    combat()

    # needs tuning
    move(9000, -32767, 4.4)
    move(-32767, 6500, 8.5)
    move(0, 32767, 3.5)
    press(X)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(-32767, -2150, 0.7)
    press(A)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, 32767, 4.8)
    press(X)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(32767, 16000, 0.2)
    press(A)
    time.sleep(LOAD_TIME)
    move(-10000, -32767, 3.3)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, 5000, 5.5)
    press(X)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-20000, -20000, 0.1)
    press(A)
    time.sleep(LOAD_TIME)
    move(-10000, -32767, 3.3)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, 32767, 0.8)
    move(-32767, 0, 5.6)
    move(0, 32767, 3.7)
    press(X)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(10000, 32767, 0.2)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, -32767, 6.7)
    move(-32767, 32767, 10.5)
    move(32767, 32767, 6.7)
    move(32767, -32767, 2.7)
    press(X)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(32767, 32767, 0.2)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, 32767, 5.9)
    press(X)
    combat()


def jarilo():
    press(MAP)
    time.sleep(LOAD_TIME)
    press(X)
    time.sleep(LOAD_TIME)
    move(7000, 20000, 0.2)
    press(A)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(32767, -2000, 0.47)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, -24000, 6.5)
    press(X)
    combat()

    move(-25000, 32767, 3.0)
    move(25000, 32767, 2.5)
    move(32767, -4000, 4.5)
    press(X)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(0, 32767, 0.3)
    press(A)
    move(-32767, -10000, 13.5)
    press(X)
    combat()

    move(32767, -5000, 5.3)
    press(X)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(10500, 32767, 0.29)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 4.5)
    press(X)
    combat()

    move(0, -32767, 4.0)
    move(32767, -32767, 2.0)
    press(X)
    combat()

    press(MAP)
    move(-4000, -32767, 0.45)
    press(A)
    move(-32767, 3500, 5.8)
    press(X)
    combat()

    move(-32767, 20000, 1.0)
    move(-32767, 12000, 4.0)
    move(9500, 32767, 5.5)
    press(X)
    combat()

    move(5000, 32767, 2.0)
    press(X)
    combat()

    press(MAP)
    move(-32767, -9000, 0.6)
    press(A)
    move(0, -32767, 5.5)
    move(-32767, 0, 6.4)
    press(X)
    combat()


spaceStation()
# jarilo()


# # reset gamepad to default state
# gamepad.reset()

# gamepad.update()

# time.sleep(1.0)
