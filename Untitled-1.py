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
LOAD_TIME = 2.3

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


def combat():
    press(X)
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

        menu = pyautogui.locateOnScreen("menu.png", confidence=0.51)

        if cv2.pollKey() != -1 or menu:
            cv2.destroyAllWindows()
            break
    time.sleep(LOAD_TIME)


def spaceStation():
    #############
    # Base Zone #
    #############

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
    move(0, -32767, 4.4)
    combat()

    ################
    # Storage Zone #
    ################

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(-32767, 0, 0.4)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 6.1)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, 32767, 0.1)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 6.1)
    move(-32767, 0, 3.2)
    move(0, 32767, 6.2)
    move(-32767, 0, 1.7)
    move(-7000, -32767, 5.5)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(5200, 0, 0.1)
    press(A)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 1.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, -32767, 0.1)
    press(A)
    time.sleep(LOAD_TIME)
    move(-6500, 32767, 4.6)
    move(-32767, 0, 2.1)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(32767, -4000, 0.5)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, -25000, 3.5)
    move(-32767, 10000, 2.5)
    move(-16000, 32767, 6.0)
    move(32767, 20000, 1.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(6500, 6500, 0.5)
    press(A)
    press(A)
    press(A)
    time.sleep(LOAD_TIME)
    move(9000, -32767, 3.0)
    move(32767, 0, 0.5)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-28000, -23000, 0.05)
    press(A)
    press(A)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, -15000, 2.0)
    move(-32767, 11000, 2.0)
    move(-32767, -7000, 3.3)
    combat()

    ###############
    # Supply Zone #
    ###############

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(-32767, -2150, 0.7)
    press(A)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, 32767, 4.8)
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
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(9000, 32767, 0.22)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, -32767, 6.7)
    move(-32767, 32767, 10.5)
    move(32767, 32767, 6.7)
    move(32767, -32767, 2.7)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(32767, 32767, 0.2)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, 32767, 5.9)
    combat()


def jarilo():
    ########################
    # Outlying Snow Plains #
    ########################

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
    move(-32767, -24000, 5.3)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-12000, 32767, 0.3)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, -9000, 8.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(0, 32767, 0.3)
    press(A)
    move(-32767, -10000, 14.2)
    combat()

    move(32767, -5000, 5.4)
    combat()

    ##################
    # Backwater Pass #
    ##################

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(10500, 32767, 0.29)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 4.5)
    combat()

    move(0, -32767, 4.0)
    move(32767, -32767, 2.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-4000, -32767, 0.45)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, 3500, 6.4)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-6000, -32767, 0.35)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 6.0)
    move(32767, -32767, 4.7)
    combat()

    # # # # MOB HERE

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, -9000, 0.3)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 5.5)
    move(-32767, 0, 6.4)
    combat()

    #############################
    # Corridor of Fading Echoes #
    #############################

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    press(DOWN)
    move(-7000, 32767, 0.2)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, 0, 1.4)
    move(0, 32767, 2.5)
    move(-32767, 0, 4.2)
    move(0, 32767, 5.8)
    move(32767, 32767, 1.7)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, -12000, 0.25)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, 0, 1.4)
    move(0, 32767, 2.5)
    move(-32767, 0, 4.2)
    move(0, 32767, 5.8)
    move(32767, 32767, 5.9)
    move(32767, -32767, 3.0)
    move(0, -32767, 2.5)
    move(-32767, -32767, 2.3)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, -2000, 0.13)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 1.1)
    move(-32767, 0, 10.4)
    move(-32767, 32767, 1.5)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(24000, 32767, 0.33)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, -28000, 7.5)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-11000, -32767, 0.92)
    press(A)
    time.sleep(LOAD_TIME)
    move(14000, 32767, 4.9)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(10000, -32767, 0.5)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 4.9)
    move(-32767, 0, 1.1)
    combat()
    move(-32767, 0, 1.1)
    combat()
    move(-32767, 0, 1.1)
    combat()
    move(-32767, 0, 1.1)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(20000, -10000, 0.25)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 4.9)
    move(-32767, 0, 3.1)
    move(0, -32767, 6.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(20000, -10000, 0.3)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 4.9)
    move(-32767, 0, 3.1)
    move(0, -32767, 8.0)
    move(32767, 0, 0.3)
    move(0, -32767, 4.3)
    move(32767, 0, 2.1)
    combat()
    move(32767, 0, 2.1)
    combat()
    move(32767, 0, 2.1)
    combat()
    move(32767, 32767, 1.0)
    combat()
    move(32767, 32767, 1.0)
    combat()
    move(0, 32767, 1.0)
    combat()
    move(0, 32767, 1.0)
    combat()

    ###################
    # Everwinter Hill #
    ###################

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(-10000, -10000, 0.22)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, -7500, 6.1)
    combat()

    move(0, 32767, 2.2)
    move(32767, 10000, 2.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, -25000, 0.5)
    press(A)
    press(A)
    press(A)
    time.sleep(LOAD_TIME)

    move(0, 32767, 7.0)
    move(-32767, 0, 8.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, -32767, 0.23)
    press(A)
    press(A)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, 32767, 7.0)
    move(-32767, 0, 8.0)
    move(-32767, 4000, 2.0)
    combat()
    move(-32767, 7000, 2.0)
    combat()

    ##############
    # Great Mine #
    ##############

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    press(DOWN)
    move(0, -32767, 0.5)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, -5000, 8.0)
    combat()

    move(-32767, -5000, 3.0)
    combat()

    move(-32767, 0, 2)
    move(18000, 32767, 3.2)
    move(32767, 20000, 5.0)
    move(-10000, 32767, 4.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(32767, -32767, 0.1)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, -32767, 3.0)
    move(32767, 0, 1.0)
    combat()
    move(32767, 0, 1.0)
    combat()
    move(32767, 0, 1.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, -32767, 0.1)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, -32767, 3.0)
    move(32767, 0, 4.0)
    move(32767, 32767, 1.4)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, 0, 0.1)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, 0, 6.0)
    move(32767, 28000, 1.5)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, 0, 0.1)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, 0, 6.0)
    move(32767, 28000, 1.5)
    move(0, 32767, 4.0)
    move(32767, 0, 1.0)
    combat()
    move(32767, 0, 1.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, 32767, 0.1)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, 20000, 2.0)
    move(-32767, -10000, 6.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(10000, 0, 0.2)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, 20000, 2.0)
    move(-32767, -10000, 6.0)
    move(0, 32767, 1.0)
    combat()
    move(0, 32767, 1.0)
    combat()
    move(0, 32767, 1.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(32767, -20000, 0.1)
    press(A)
    time.sleep(LOAD_TIME)
    move(-32767, 20000, 2.0)
    move(-32767, -400, 5.5)
    move(0, 32767, 4.0)
    move(32767, 0, 1.4)
    combat()

    ##############
    # Rivet Town #
    ##############

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(4000, 32767, 0.3)
    press(A)
    time.sleep(LOAD_TIME)
    move(23000, -32767, 1.9)
    move(-32767, 0, 7.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(32767, 32767, 0.1)
    press(A)
    time.sleep(LOAD_TIME)
    move(23000, -32767, 1.9)
    move(-32767, 0, 7.0)
    move(0, 32767, 12.5)
    move(-32767, 3000, 1.8)
    move(0, 32767, 3.0)
    combat()
    move(0, 32767, 1.0)
    combat()
    move(0, 32767, 1.0)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, 32767, 0.2)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 1.2)
    move(32767, 0, 1.8)
    move(0, -32767, 1.6)
    move(32767, -32767, 1.2)
    move(32767, 0, 2.7)
    move(32767, 32767, 1.2)
    combat()
    move(32767, 32767, 1.2)
    combat()
    move(32767, 32767, 1.2)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, 32767, 0.2)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, -32767, 1.2)
    move(32767, 0, 1.8)
    move(0, -32767, 1.6)
    move(32767, -32767, 1.2)
    move(32767, 0, 2.7)
    move(32767, 32767, 5.5)
    combat()

    ####################
    # Robot Settlement #
    ####################

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(-32767, -13000, 0.4)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, -32767, 1.5)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, 0, 0.2)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, -15000, 7.0)
    move(10000, -32767, 1.3)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, -32767, 0.25)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, -15000, 3.0)
    move(-7000, -32767, 7.0)
    move(-10000, -32767, 10.0)
    move(32767, -24000, 2.0)
    move(-32767, -24000, 3.7)
    move(0, -32767, 0.8)
    press(X)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, -6000, 0.25)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, -15000, 3.0)
    move(-7000, -32767, 7.0)
    move(-10000, -32767, 10.0)
    move(32767, -24000, 2.0)
    move(32767, 0, 0.3)
    combat()

    press(MAP)
    time.sleep(LOAD_TIME)
    move(-32767, -11000, 0.27)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, -15000, 3.0)
    move(-7000, -32767, 7.0)
    move(-10000, -32767, 10.0)
    move(32767, -24000, 2.0)
    move(32767, 0, 2.2)
    move(0, 32767, 1.4)
    combat()


def xianzhou():
    #############
    # Cloudford #
    #############

    press(MAP)


# spaceStation()
# jarilo()
# xianzhou()


# # reset gamepad to default state
# gamepad.reset()

# gamepad.update()

# time.sleep(1.0)
