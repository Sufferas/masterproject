import time
from pynput.keyboard import Key, Controller, Listener
import re
from deepLearning.chat import get_trained_model
import pyautogui


keyboard = Controller()

debug = True


def hello_world():
    if debug is True:
        print(" Hello World !!! ")
        print(" Time to Sleep 10 sec")
        time.sleep(10)


def python_main_function(param=None):
    if debug is True:
        print(" Time to Sleep 10 sec then work!!")
        print(param)
        time.sleep(10)
    keyboard.type('# if __name__ == "__main__":\n\n')


def python_while_loop(param=None):
    if debug is True:
        print(" Time to Sleep 10 sec then work!!")
        time.sleep(10)
    keyboard.type('# as long as while is true the while remains active --> set while to false to exit the loop.\n')
    keyboard.type('# example 1:\n')
    keyboard.type('# while i < 6: \n')
    keyboard.type('# \ti = i + 1\n')
    keyboard.type('# \tprint(i) \n\n')

    keyboard.type('# example 2:\n')
    keyboard.type('# while i is True: \n')
    keyboard.type('# \tprint("i is True") \n\n')


def python_for_loop(param=None):
    if debug is True:
        print(" Time to Sleep 10 sec then work!!")
        time.sleep(10)
    keyboard.type('# examples 1: \n')
    keyboard.type('# fruits = ["apple", "banana", "cherry"] \n')
    keyboard.type('# for x in fruits: \n')
    keyboard.type('# \tprint(x) \n\n')

    keyboard.type('# examples 2: \n')
    keyboard.type('# for x in range(6): \n')
    keyboard.type('# \tprint(x) \n\n')

    keyboard.type('# examples 3: \n')
    keyboard.type('# for x in range(2, 6): \n')
    keyboard.type('# \tprint(x) \n\n')

    keyboard.type('# examples 4: \n')
    keyboard.type('# for x in range(2, 30, 3): \n')
    keyboard.type('# \tprint(x) \n\n')


def python_function(param=None):
    if debug is True:
        print(" Time to Sleep 10 sec then work!!")
        time.sleep(10)

    keyboard.type('# examples 1: \n')
    keyboard.type('# def example_function(): \n')
    keyboard.type('# \tprint("function without parameter ") \n\n')
    keyboard.type('# examples 2: \n')
    keyboard.type('# def example_function(param1, param2): \n')
    keyboard.type('# \tprint(param1, param2)\n')
    keyboard.type('# \tprint("function with two parameters") \n\n')


def move_mouse(param=None):
    if debug is True:
        print(" Time to Sleep 10 sec then work!!")
        time.sleep(10)

    status, text = get_trained_model("deepLearning\\TrainedModels\\mouse_move.pth",
                                     'deepLearning\\jsonFiles\\mouse_move.json', param)

    leave = True
    while leave:

        match = re.search(r'\d+', param)
        if match:
            leave = False
            number = int(match.group())
            print(number)
            try:
                if text == "left":
                    pyautogui.moveRel(-number, 0, duration=1)
                elif text == "right":
                    pyautogui.moveRel(number, 0, duration=1)
                elif text == "up":
                    pyautogui.moveRel(0, -number, duration=1)
                elif text == "down":
                    pyautogui.moveRel(0, number, duration=1)
                elif text == "right_mouse":
                    pyautogui.click(button='right')
                elif text == "left_mouse":
                    pyautogui.click(button='left')
            except:
                print("out off move")





        else:
            print("number not found")
            print("say it again")









