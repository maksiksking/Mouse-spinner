import pyautogui
import time

screenSize = pyautogui.size()

x = screenSize[0]/2
y = screenSize[1]/2

time.sleep(3)

# SETTINGS

pyautogui.PAUSE = 0

# Multiplier
size = 100
# Duration
speed = 0.2
# Incrementation
step = 0.0001

pyautogui.moveTo(x, y, 0)

a = step

loopStart = True

while True:
    if loopStart:
        while True:
            a += step
            b = -(a - 2) * 0.5 - 1

            pyautogui.moveTo(x + a * size, y + b * size, speed * 0.5, pyautogui.linear)
            if a >= 2:
                break

    while True:
        a += step
        b = (((a - 2) ** 4) * 0.8) - 1

        pyautogui.moveTo(x + a * size, y + b * size, speed * 0.5, pyautogui.linear)
        if a >= 3:
            a += step
            break

    while True:
        a -= step
        b = -(((a - 2) ** 4) * 0.8) + 1

        pyautogui.moveTo(x + a * size, y + b * size, speed * 0.5, pyautogui.linear)
        if a <= 2:
            a -= step * 2
            break

    while True:
        a -= step
        b = a * 0.5

        pyautogui.moveTo(x + a * size, y + b * size, speed * 0.5, pyautogui.linear)
        if a <= -2:
            a += step
            break

    # Side 2

    while True:
        a -= step
        b = (((a + 2) ** 4) * 0.8) - 1

        pyautogui.moveTo(x + a * size, y + b * size, speed * 0.5, pyautogui.linear)
        if a <= -3:
            a -= step
            break

    while True:
        a += step
        b = -(((a + 2) ** 4) * 0.8) + 1

        pyautogui.moveTo(x + a * size, y + b * size, speed * 0.5, pyautogui.linear)
        if a >= -2:
            a += step*2
            break

    while True:
        a += step
        b = -(a + 2) * 0.5 + 1

        pyautogui.moveTo(x + a * size, y + b * size, speed * 0.5, pyautogui.linear)
        if a >= 2:
            loopStart = False
            break

# I think this is also accomplishable by running stuff in parallel but this weird method is better anyway.
# Ideally you want to use a proper library like now broken Autopy for this.
