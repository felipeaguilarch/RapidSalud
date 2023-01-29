import pyautogui
import keyboard
import time

start = False
pyautogui.FAILSAFE=False

positions = []
FILTER_SIZE = 10

def stabilize_mouse():
    global FILTER_SIZE
    x, y = pyautogui.position()
    positions.append((x, y))
    if len(positions) > FILTER_SIZE:
        positions.pop(0)

    smoothed_x = sum(x for x, y in positions) / len(positions)
    smoothed_y = sum(y for x, y in positions) / len(positions)

    pyautogui.moveTo(smoothed_x, smoothed_y, duration=0.1)

    if abs(x-smoothed_x) > 10 and abs(y-smoothed_y) > 10:
        FILTER_SIZE = 30
    else:
        FILTER_SIZE = 10

    time.sleep(0.01)

while not start:

    stabilize_mouse()

    if keyboard.is_pressed('esc'):
        print('Finish')
        start = True