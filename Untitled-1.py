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
LOAD_TIME = 3.0

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
    time.sleep(LOAD_TIME)
    while True:
        screenshot = pyautogui.screenshot(
            region=(
                gameWindow.top,
                gameWindow.left,
                gameWindow.width * 0.05,
                gameWindow.height * 0.1,
            )
        )
        screenshot = np.array(screenshot)

        cv2.imshow("title", screenshot)

        clear = pyautogui.locateOnScreen("menu.png", confidence=0.92)
        notClear = pyautogui.locateOnScreen("notification.png", confidence=0.852)

        if cv2.pollKey() != -1 or clear or notClear:
            cv2.destroyAllWindows()
            break

    time.sleep(LOAD_TIME)


def warp(x, y, duration):
    press(MAP)
    time.sleep(LOAD_TIME)
    move(x, y, duration)
    press(A)
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

    warp(-32767, 32767, 0.1)
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
    move(0, -32767, 2.0)
    combat()

    warp(-27777, -27777, 0.1)
    move(-6500, 32767, 4.6)
    move(-32767, 0, 2.1)
    combat()

    warp(32767, -4000, 0.5)
    move(-32767, -25000, 3.5)
    move(-32767, 10000, 2.5)
    move(-16000, 32767, 6.2)
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

    warp(32767, 16000, 0.2)
    move(-10000, -32767, 3.3)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, 5000, 5.5)
    combat()

    warp(-15000, -15000, 0.1)
    move(-10000, -32767, 3.3)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, 32767, 0.8)
    move(-32767, 0, 5.6)
    move(0, 32767, 3.7)
    combat()

    warp(9000, 32767, 0.22)
    move(-32767, -32767, 6.7)
    move(-32767, 32767, 10.5)
    move(32767, 32767, 6.7)
    move(32767, -32767, 2.7)
    combat()

    warp(32767, 32767, 0.2)
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

    warp(-12000, 32767, 0.25)
    move(-32767, -9000, 8.0)
    combat()

    warp(0, 32767, 0.3)
    move(-32767, -10000, 14.2)
    combat()

    warp(32767, 10000, 0.33)
    move(-32767, -3000, 14.8)
    move(0, 32767, 1.6)
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

    warp(-2000, -32767, 0.3)
    move(-32767, 3500, 5.7)
    combat()

    warp(-8000, -32767, 0.35)
    move(0, -32767, 6.0)
    move(32767, -32767, 3.8)
    combat()

    warp(-32767, -9000, 0.3)
    move(0, -32767, 6.0)
    move(32767, -32767, 3.8)
    move(32767, 0, 1.2)
    combat()
    move(32767, 0, 1.2)
    combat()

    warp(-32767, -18000, 0.3)
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

    warp(-32767, -12000, 0.25)
    move(-32767, 0, 1.4)
    move(0, 32767, 2.5)
    move(-32767, 0, 4.2)
    move(0, 32767, 5.8)
    move(32767, 32767, 5.9)
    move(32767, -32767, 3.0)
    move(0, -32767, 2.5)
    move(-32767, -32767, 2.3)
    combat()

    warp(-32767, -2000, 0.13)
    move(0, -32767, 1.1)
    move(-32767, 0, 10.4)
    move(-32767, 32767, 1.5)
    combat()

    warp(24000, 32767, 0.33)
    move(32767, -28000, 7.5)
    combat()

    warp(-11000, -32767, 0.92)
    move(14000, 32767, 4.9)
    combat()

    warp(10000, -32767, 0.5)
    move(0, -32767, 4.9)
    move(-32767, 0, 1.1)
    combat()
    move(-32767, 0, 1.1)
    combat()
    move(-32767, 0, 1.1)
    combat()
    move(-32767, 0, 1.1)
    combat()

    warp(20000, -10000, 0.25)
    move(0, -32767, 4.9)
    move(-32767, 0, 3.1)
    move(0, -32767, 6.0)
    combat()

    warp(20000, -10000, 0.3)
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

    warp(-2000, -32767, 0.2)
    move(-32767, -7500, 7.4)
    move(0, 32767, 3.5)
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
    move(-32767, -32767, 0.25)
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

    warp(5000, -32767, 0.22)
    move(-32767, -5000, 8.0)
    move(-32767, 10000, 3.0)
    move(5000, 32767, 1.4)
    move(32767, 0, 6.2)
    move(15000, 32767, 3.2)
    combat()

    warp(32767, -32767, 0.1)
    move(32767, -32767, 3.0)
    move(32767, 0, 1.0)
    combat()
    move(32767, 0, 1.0)
    combat()
    move(32767, 0, 1.0)
    combat()

    warp(-32767, -32767, 0.1)
    move(32767, -32767, 3.0)
    move(32767, 0, 4.0)
    move(32767, 32767, 1.1)
    combat()

    warp(-32767, 0, 0.1)
    move(32767, 0, 6.0)
    move(32767, 28000, 1.5)
    combat()

    warp(-32767, 0, 0.1)
    move(32767, 0, 6.0)
    move(32767, 28000, 1.5)
    move(0, 32767, 4.0)
    move(32767, 0, 1.0)
    combat()
    move(32767, 0, 1.0)
    combat()

    warp(-32767, 32767, 0.1)
    move(-32767, 20000, 2.0)
    move(-32767, -10000, 6.0)
    combat()

    warp(10000, 0, 0.2)
    move(-32767, 20000, 2.0)
    move(-32767, -10000, 6.0)
    move(0, 32767, 1.0)
    combat()
    move(0, 32767, 1.0)
    combat()
    move(0, 32767, 1.0)
    combat()

    warp(32767, -20000, 0.1)
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

    warp(32767, 32767, 0.1)
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

    warp(-30000, 32767, 0.23)
    move(0, -32767, 1.2)
    move(32767, 0, 1.8)
    move(0, -32767, 1.6)
    move(32767, -32767, 1.2)
    move(32767, 0, 2.7)
    move(32767, 32767, 1.2)
    combat()
    move(32767, 32767, 1.2)
    combat()

    warp(-32767, 32767, 0.2)
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

    warp(-32767, 0, 0.2)
    move(32767, -15000, 7.0)
    move(10000, -32767, 1.1)
    combat()

    warp(-32767, -32767, 0.25)
    move(32767, -15000, 3.0)
    move(-7000, -32767, 7.0)
    move(-10000, -32767, 9.5)
    move(32767, -24000, 2.0)
    move(-32767, -24000, 3.7)
    move(0, -32767, 1.0)
    combat()

    warp(-32767, -6000, 0.25)
    move(32767, -15000, 3.0)
    move(-7000, -32767, 7.0)
    move(-10000, -32767, 9.6)
    move(32767, -24000, 1.9)
    move(32767, 0, 0.3)
    combat()

    warp(-32767, -11000, 0.27)
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
    time.sleep(LOAD_TIME)
    press(X)
    time.sleep(LOAD_TIME)
    move(32767, -21000, 0.3)  ##
    press(A)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(-32767, 2000, 0.1)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, 0, 1.7)
    move(0, -32767, 3.8)
    move(32767, 0, 6.0)
    move(4000, 32767, 2.1)
    combat()

    warp(-2000, -32767, 0.21)
    move(32767, 0, 1.7)
    move(0, -32767, 3.8)
    move(32767, 0, 6.0)
    move(-7000, 32767, 4.2)
    combat()

    warp(5000, -32767, 0.205)
    move(32767, 0, 1.7)
    move(0, -32767, 5.8)
    move(32767, 0, 1.7)
    move(0, -32767, 10.8)
    move(32767, 0, 1.0)
    combat()
    move(32767, 0, 1.0)
    combat()
    move(32767, 0, 1.0)
    combat()

    warp(-32767, -32767, 0.2)
    move(32767, 0, 1.7)
    move(0, -32767, 5.8)
    move(32767, 0, 1.7)
    move(0, -32767, 10.8)
    move(32767, 0, 2.7)
    move(0, -32767, 4.0)
    combat()

    warp(-6000, -32767, 0.5)
    move(32767, -32767, 1.3)
    move(32767, -15000, 2.0)
    combat()

    warp(7000, -32767, 0.64)
    move(32767, 0, 5.0)
    move(0, -32767, 4.0)
    move(-32767, -32767, 2.0)
    combat()

    warp(22000, -32767, 0.14)
    move(32767, 0, 5.0)
    move(0, -32767, 6.65)
    move(32767, 0, 3.0)
    combat()
    move(0, -32767, 1.0)
    combat()

    warp(22000, -32767, 0.16)
    move(32767, 0, 5.0)
    move(0, -32767, 6.65)
    move(32767, 0, 3.0)
    move(-32767, 32767, 1.2)
    combat()

    warp(22000, -32767, 0.16)
    move(32767, 0, 10.0)
    move(0, -32767, 2.4)
    combat()

    move(0, 32767, 3.4)
    move(-32767, 6000, 2.75)
    combat()

    #####################
    # Stargazer Navalia #
    #####################

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(32767, 32000, 0.52)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, 25000, 9.7)
    move(-32767, -3000, 2.0)
    combat()

    warp(32767, 20000, 0.2)
    move(32767, 25000, 9.7)
    move(-32767, -6000, 8.7)
    move(-32767, -20000, 2.4)
    move(0, 32767, 4.0)
    combat()
    move(32767, 0, 1.0)
    combat()
    move(32767, 0, 1.0)
    combat()

    warp(10000, 32767, 0.195)
    move(32767, 25000, 9.7)
    move(-32767, -6000, 8.5)
    move(-32767, -20000, 2.4)
    move(0, 32767, 2.0)
    move(-13000, 32767, 4.7)
    combat()

    warp(7000, 32767, 0.3)
    move(32767, 25000, 9.7)
    move(-32767, -6000, 8.7)
    move(-32767, -20000, 2.4)
    move(0, 32767, 2.0)
    move(-32767, 32767, 7.0)
    move(32767, 0, 1.0)
    combat()

    warp(-6000, -32767, 0.5)
    move(32767, -6000, 8.4)
    combat()
    move(0, 32767, 1.0)
    combat()
    move(0, 32767, 1.0)
    combat()
    move(0, 32767, 1.0)
    combat()

    warp(32767, -2000, 0.2)
    move(32767, -6000, 8.4)
    move(0, 32767, 3.2)
    move(32767, 0, 10)
    move(25000, -32767, 4.0)
    move(32767, 0, 2.6)
    move(0, 32767, 1.8)
    combat()

    warp(32767, -2000, 0.5)
    move(32767, -6000, 8.4)
    move(0, 32767, 3.2)
    move(32767, 0, 10)
    move(0, -32767, 4.0)
    combat()
    move(0, -32767, 1.0)
    combat()

    warp(32767, 32767, 0.24)
    move(0, 32767, 1.2)
    move(32767, 0, 0.6)
    move(0, -32767, 4.3)
    move(-32767, 0, 7.1)
    move(0, -32767, 2.0)
    move(-32767, 0, 1.0)
    combat()
    move(0, -32767, 1.0)
    combat()
    move(0, -32767, 1.0)
    combat()

    warp(32767, 32767, 0.24)
    move(0, 32767, 1.2)
    move(32767, 0, 0.6)
    move(0, -32767, 4.3)
    move(-32767, 0, 6.7)
    move(12000, 32767, 1.5)
    move(0, 32767, 4.4)
    move(-32767, 0, 2.4)
    move(0, -32767, 2.7)
    combat()

    warp(28000, 32767, 0.2)
    move(-32767, 32767, 0.5)
    move(0, 32767, 1.0)
    move(32767, 0, 2.5)
    move(0, 32767, 1.0)
    combat()
    move(0, 32767, 1.0)
    combat()
    move(-327670, 0, 1.0)
    combat()

    warp(32767, -32767, 0.12)
    move(0, -32767, 0.4)
    move(32767, 0, 11.0)
    combat()

    warp(-2000, -32767, 0.3)
    move(0, -32767, 0.3)
    move(32767, 0, 11.0)
    move(0, -32767, 3.9)
    combat()

    warp(-32767, -32767, 0.2)
    move(32767, -32767, 3.3)
    combat()

    #########################
    # Divination Commission #
    #########################

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    press(DOWN)
    move(-15000, -32767, 0.88)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, 32767, 4.0)
    move(-32767, 22000, 3.3)
    combat()
    combat()
    combat()

    warp(-32767, -23000, 0.2)
    move(0, 32767, 4.0)
    move(-32767, 22000, 3.3)
    move(-32767, 10000, 4.7)
    move(0, 32767, 5.7)
    combat()

    warp(-32767, -22000, 0.42)
    move(0, 32767, 4.0)
    move(-32767, 22000, 3.3)
    move(-32767, 2000, 12.0)
    move(0, 32767, 1.0)
    combat()
    move(-32767, 0, 1.0)
    combat()
    move(0, -32767, 1.0)
    combat()
    move(32767, 0, 1.0)
    combat()
    move(0, 32767, 1.0)
    combat()

    warp(-15000, -32767, 0.5)
    move(0, 32767, 4.0)
    move(-32767, 22000, 3.3)
    move(-32767, 2000, 12.0)
    move(-10000, -32767, 3.5)
    move(-2000, -32767, 10.0)
    combat()
    move(0, -32767, 1.0)
    combat()

    warp(0, 32767, 0.85)
    move(0, -32767, 4.25)
    move(32767, -32767, 3.8)
    move(32767, 32767, 1.0)
    combat()

    move(0, -32767, 1.0)
    combat()
    move(0, -32767, 1.0)
    combat()

    warp(0, 32767, 0.17)
    move(0, -32767, 4.1)
    move(32767, -32767, 5.2)
    move(-32767, -32767, 3.5)
    move(-32767, 32767, 1.0)
    combat()

    move(0, -32767, 1.0)
    combat()
    move(0, -32767, 1.0)
    combat()

    warp(0, 32767, 0.17)
    move(0, -32767, 3.8)
    move(32767, -32767, 11.0)
    move(32767, 0, 4.0)
    move(32767, 15000, 2.0)
    move(32767, -15000, 2.0)
    move(32767, 0, 3.9)
    move(32767, 32767, 4.0)
    move(32767, 0, 1.0)
    combat()

    warp(32767, -10000, 0.6)
    move(0, -32767, 25.6)
    combat()

    warp(0, -32767, 0.7)
    move(0, -32767, 22.6)
    move(-32767, -5000, 5.0)
    move(-32767, -32767, 3.2)
    combat()

    move(25000, 32767, 1.0)
    combat()
    move(-25000, -32767, 1.0)
    combat()

    warp(-5000, -32767, 0.65)
    move(0, -32767, 22.3)
    move(32767, 0, 2.0)
    move(32767, -10000, 6.2)
    move(-10000, -32767, 3.0)
    move(0, -32767, 2.8)
    move(32767, -32767, 2.3)
    combat()

    ##########################
    # Artisanship Commission #
    ##########################

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(24500, 32767, 0.37)
    press(A)
    time.sleep(LOAD_TIME)
    move(0, 32767, 10.8)
    move(-32767, 0, 0.8)
    move(0, -32767, 0.2)
    combat()

    warp(5000, -32767, 0.2)
    move(0, 32767, 5.2)
    move(32767, 2000, 7.7)
    combat()

    warp(-32767, -32767, 0.25)
    move(0, 32767, 10.8)
    move(32767, 0, 4.2)
    move(-3000, 32767, 5.3)
    move(32767, 4000, 1.5)
    move(0, -32767, 0.2)
    combat()
    combat()

    warp(-32767, -14000, 0.7)
    move(0, 32767, 6.8)
    move(32767, 0, 1.0)
    combat()
    move(32767, 0, 1.0)
    combat()

    warp(32767, -32767, 0.24)
    move(0, 32767, 6.8)
    move(32767, 0, 6.0)
    combat()

    warp(28000, -32767, 0.25)
    move(0, 32767, 6.8)
    move(32767, 0, 6.6)
    move(0, -32767, 0.5)
    move(-32767, 0, 4.3)
    move(0, -32767, 2.7)
    move(32767, 0, 1.4)
    combat()

    move(32767, 32767, 0.5)
    combat()
    move(32767, 32767, 0.5)
    combat()
    move(0, -32767, 0.5)
    combat()

    warp(6000, -32767, 0.2)
    move(-32767, -5000, 3.5)
    move(0, 32767, 5.0)
    move(-32767, 7000, 6.1)
    combat()
    move(-32767, -32767, 1.0)
    combat()
    move(32767, 0, 1.0)
    combat()
    move(-32767, -32767, 1.0)
    combat()
    move(-32767, -32767, 1.0)
    combat()

    warp(8000, 32767, 0.28)
    move(-32767, -10000, 8.1)
    move(-32767, 0, 2.5)
    combat()

    warp(-7000, 32767, 0.28)
    move(-32767, -10000, 8.1)
    move(-32767, 0, 2.5)
    move(-32767, -32767, 1.5)
    move(-32767, 0, 5.0)
    move(-32767, 32767, 2.1)
    combat()
    move(32767, 32767, 0.3)
    combat()
    move(-32767, -32767, 0.3)
    combat()

    warp(-5000, 32767, 0.47)
    move(-32767, -10000, 8.1)
    move(-32767, 0, 2.5)
    move(-32767, -32767, 1.5)
    move(-32767, 2000, 5.0)
    move(-32767, 32767, 2.4)
    move(-32767, 2000, 11.0)
    move(-2000, 32767, 4.0)
    move(-32767, 6000, 4.0)
    move(-32767, 0, 5.5)
    combat()

    warp(2700, 32767, 1.0)
    move(-32767, -10000, 8.1)
    move(-32767, 0, 2.5)
    move(-32767, -32767, 1.5)
    move(-32767, 2000, 5.0)
    move(-32767, 32767, 2.4)
    move(-32767, 2000, 11.0)
    move(-2000, 32767, 4.0)
    move(-32767, 6000, 4.0)
    move(-32767, 0, 7.8)
    move(-32767, -32767, 2.5)
    combat()

    warp(32767, 25000, 0.65)
    move(-32767, 0, 1.0)
    move(0, -32767, 0.6)
    move(32767, 0, 1.9)
    move(0, 32767, 2.0)
    move(32767, 0, 3.1)
    move(0, -32767, 4.0)
    move(32767, 0, 0.5)
    combat()

    move(-32767, 32767, 1.2)
    combat()
    move(-32767, -32767, 1.2)
    combat()
    move(32767, -32767, 1.2)
    combat()
    move(32767, 32767, 1.2)
    combat()

    warp(3300, 32767, 0.3)
    move(-32767, 0, 1.0)
    move(0, -32767, 0.6)
    move(32767, 0, 1.9)
    move(0, 32767, 2.0)
    move(32767, 0, 3.1)
    move(0, -32767, 4.0)
    move(20000, 32767, 6.8)
    move(0, 32767, 3.8)
    move(-32767, 0, 1.2)
    move(-32767, 32767, 1.2)
    combat()

    ######################
    # Alchemy Commission #
    ######################

    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(-3000, -32767, 0.8)
    press(A)
    time.sleep(1.0)
    time.sleep(LOAD_TIME)
    move(0, -32767, 5.0)
    move(-32767, -32767, 1.0)
    combat()
    move(-32767, -32767, 1.0)
    combat()

    warp(0, -32767, 0.1)
    move(0, -32767, 5.0)
    move(-32767, -32767, 8.0)
    combat()

    warp(-17000, -32767, 0.31)
    move(0, -32767, 1.0)
    move(32767, 0, 5.2)
    move(0, -32767, 5.8)
    move(-32767, -32767, 10.0)
    move(-25000, -32767, 9.5)
    combat()

    warp(-12000, -32767, 0.61)
    move(0, -32767, 1.0)
    move(32767, 0, 5.2)
    move(0, -32767, 5.8)
    move(-32767, -32767, 10.0)
    move(-12000, -32767, 9.5)
    combat()

    move(-32767, 32767, 1.2)
    combat()
    move(-32767, -32767, 1.2)
    combat()
    move(32767, -32767, 1.2)
    combat()
    move(32767, 32767, 1.2)
    combat()

    warp(12000, 32767, 0.3)
    move(-16000, 32767, 3.0)
    move(-26000, 32767, 3.0)
    move(-32767, 25000, 3.0)
    move(-32767, 0, 3.0)
    move(-32767, -10000, 3.0)
    move(-32767, -17000, 8.5)
    combat()

    warp(10000, -32767, 0.55)
    move(-13000, -32767, 13.2)
    move(32767, -25000, 7.2)
    combat()

    warp(-12000, 32767, 0.5)
    move(1000, 32767, 6.8)
    move(32767, 0, 3.1)
    move(0, -32767, 3.4)
    move(32767, 0, 3.9)
    combat()

    warp(32767, 25000, 0.2)
    move(1000, 32767, 6.8)
    move(0, 32767, 2.0)
    move(-18000, 32767, 3.3)
    move(-32767, 0, 1.7)
    move(0, -32767, 5.0)
    move(-32767, 0, 0.8)
    move(0, 32767, 1.4)
    combat()

    warp(-18000, 32767, 0.31)
    move(1000, 32767, 6.8)
    move(0, 32767, 2.0)
    move(-18000, 32767, 3.3)
    move(-32767, 0, 1.7)
    move(0, 32767, 10.0)
    move(-32767, 32767, 1.8)
    move(-32767, 0, 4.6)
    move(0, 32767, 7.0)
    move(-32767, 32767, 1.7)
    move(-32767, -5000, 1.2)
    combat()

    warp(-5000, 32767, 1.0)
    move(-10000, 32767, 2.7)
    move(22000, 32767, 4.0)
    move(17000, 32767, 4.0)
    move(32767, 0, 4.0)
    move(-32767, 12000, 1.0)
    combat()

    warp(32767, 0, 0.3)
    move(-10000, 32767, 2.7)
    move(22000, 32767, 4.0)
    move(17000, 32767, 4.0)
    move(32767, 0, 4.0)
    move(32767, 30000, 2.0)
    move(32767, 15000, 1.3)
    move(32767, -20000, 3.1)
    move(32767, 0, 1.9)
    move(0, -32767, 1.9)
    move(-32767, 20000, 2.5)
    combat()

    warp(32767, -16000, 0.37)
    move(-5000, 32767, 2.7)
    move(19000, 32767, 4.0)
    move(18000, 32767, 3.3)
    move(32767, 14000, 3.9)
    move(32767, 2000, 3.5)
    move(32767, -20000, 2.0)
    move(6000, -32767, 2.13)
    move(-16000, -32767, 2.6)
    move(0, -32767, 4.0)
    move(-32000, -32767, 3.0)
    move(-32767, 0, 2.8)
    combat()

    #########################
    # Scalegorge Waterscape #
    #########################
    press(MAP)
    time.sleep(LOAD_TIME)
    press(DOWN)
    move(32767, 0, 0.8)
    press(A)
    time.sleep(LOAD_TIME)
    move(32767, 4000, 2.5)
    move(32767, -10000, 4.5)
    move(0, -32767, 1.0)
    move(0, 32767, 1.0)
    combat()

    warp(-32767, -4000, 0.76)
    move(-32767, 0, 5.7)
    move(-32767, -16000, 3.0)
    move(-32767, 3000, 6.9)
    combat()

    warp(-2000, 32767, 0.3)
    move(-32767, 0, 5.7)
    move(-32767, -16000, 3.0)
    move(-32767, 6000, 6.5)
    move(0, 32767, 11.5)
    combat()

    warp(-15000, 32767, 0.3)
    move(-20000, -32767, 2.0)
    move(-32767, -13000, 4.5)
    move(-32767, 0, 16.0)
    combat()

    warp(-2000, 32767, 0.35)
    move(-20000, -32767, 2.0)
    move(-32767, -13000, 4.5)
    move(-32767, 0, 14.5)
    move(-7000, 32767, 3.7)
    move(32767, 32767, 10.2)
    move(0, 32767, 5.0)
    move(32767, 32767, 5.0)
    combat()
    combat()
    combat()
    combat()

    warp(32767, 22000, 0.4)
    move(32767, -32767, 4.0)
    move(2000, -32767, 7.0)
    combat()

    warp(-32767, -4000, 0.2)
    move(32767, -32767, 4.0)
    move(32767, 0, 21.5)
    combat()

    warp(-5000, -32767, 0.3)
    move(32767, -32767, 4.0)
    move(32767, 0, 19.8)
    move(0, 32767, 10.0)
    move(-32767, 0, 4.0)
    move(32767, 0, 4.0)
    combat()

    #####################
    # Return to Express #
    #####################
    press(MAP)
    time.sleep(LOAD_TIME)
    press(UP)
    press(UP)
    press(UP)
    press(UP)
    press(UP)
    press(UP)
    press(UP)
    press(UP)
    move(-32767, 32767, 0.1)
    press(A)
    time.sleep(LOAD_TIME)


spaceStation()
jarilo()
xianzhou()


# # reset gamepad to default state
gamepad.reset()
gamepad.update()
time.sleep(1.0)
