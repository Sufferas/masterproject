import time
from pynput.keyboard import Key, Controller, Listener
import re
from deepLearning.chat import get_trained_model
import pyautogui

from speech_record import from_microphone

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
            voice_to_text = from_microphone()
            status, text = get_trained_model("deepLearning\\TrainedModels\\mouse_move.pth",
                                             'deepLearning\\jsonFiles\\mouse_move.json', voice_to_text)


def py_abs():
    keyboard.type('# abs() # Returns the absolute value of the specified number.\n')


def py_all():
    keyboard.type('# all() # returns True if all elements in an iterable are true, otherwise it returns False.\n')


def py_any():
    keyboard.type('# any() # returns True if all elements in an iterable are true, otherwise it returns False\n')


def py_ascii():
    keyboard.type('# ascii() # returns a readable version of any object (strings, tuples, lists, etc.)\n')


def py_bin():
    keyboard.type('# bin() # returns the binary version of an integer\n')


def py_bool():
    keyboard.type('# bool() # returns the boolean value of a specified object\n')


def py_bytearray():
    keyboard.type('# bytearray() # returns a byte array object\n')


def py_bytes():
    keyboard.type('# bytes() # returns a bytes object\n')


def py_callable():
    keyboard.type('# callable() # returns True if the specified object is callable, otherwise it returns False\n')


def py_chr():
    keyboard.type('# chr() # returns True if the specified object is callable, otherwise it returns False\n')


def py_compile():
    keyboard.type('# compile() # Returns the specified source as a code object, ready for execution\n')


def py_complex():
    keyboard.type('# complex() # returns a complex number by specifying a real number and an imaginary number\n')


def py_delattr():
    keyboard.type('# delattr() # eletes the specified attribute from the specified object\n')


def py_dict():
    keyboard.type('# dict() # creates a dictionary (array)\n')


def py_divmod():
    keyboard.type('# divmod() # returns a tuple containing the quotient and the remainder when dividing dividend by divisor')


def py_enumerate():
    keyboard.type('# enumerate() # returns a tuple containing the quotient and the remainder when dividing dividend by divisor')


def py_eval():
    keyboard.type('# eval() # evaluates the given expression, if it is a legal Python statement')


def py_exec():
    keyboard.type('# exec() # executes the specified Python code')


def py_filter():
    keyboard.type('# filter() # returns an iterator in which the elements are filtered by a function to check whether the element is accepted or not')


def py_float():
    keyboard.type('# float() # Converts the specified value to a floating point number')


def py_format():
    keyboard.type('# format() # formats a specified value into a specific format')


def py_frozenset():
    keyboard.type('# frozenset() # returns an immutable frozenset object')


def py_getattr():
    keyboard.type('# getattr() # returns the value of the specified attribute from the specified object')


def py_globals():
    keyboard.type('# globals() # returns the global symbol table as a dictionary')


def py_hasattr():
    keyboard.type('# hasattr() # returns True if the specified object has the specified attribute, otherwise False')


def py_hex():
    keyboard.type('# hex() # converts the specified number to a hexadecimal value')


def py_id():
    keyboard.type('# id() # returns a unique ID for the specified object')


def py_input():
    keyboard.type('# input() # returns a unique ID for the specified object')


def py_int():
    keyboard.type('# int() # Converts the specified value into an integer number')


def py_isinstance():
    keyboard.type('# isinstance() # returns True if the specified object is of the specified type, otherwise False')


def py_issubclass():
    keyboard.type('# issubclass() # returns True if the specified object is a subclass of the specified object, otherwise False')


def py_iter():
    keyboard.type('# iter() # returns an iterator object')


def py_len():
    keyboard.type('# len() # returns the number of elements in an object')


def py_list():
    keyboard.type('# list() # creates a list object')


def py_locals():
    keyboard.type('# locals() # returns the local symbol table as a dictionary')


def py_map():
    keyboard.type('# map() # executes a specified function for each element in an iterable')


def py_max():
    keyboard.type('# max() # returns the element with the highest value or the element with the highest value in an iterable')


def py_memoryview():
    keyboard.type('# memoryview() # returns a memory view object from a specified object')


def py_min():
    keyboard.type('# min() # returns the element with the lowest value or the element with the lowest value in an iterable')


def py_next():
    keyboard.type('# next() # returns the next element in an iterator')


def py_object():
    keyboard.type('# object() # returns an empty object')


def py_open():
    keyboard.type('# open() # opens a file and returns it as a file object')


def py_ord():
    keyboard.type('# ord() # returns the number representing the Unicode code of a specified character')


def py_pow():
    keyboard.type('# pow() # returns the value of x as a power of y (x^y)')


def py_print():
    keyboard.type('# print() # outputs the specified message to the screen or other standard output device')


def py_range():
    keyboard.type('# range() # returns a sequence of numbers that by default starts at 0, increments by 1, and stops before a specified number')


def py_repr():
    keyboard.type('# range() # Returns a readable version of an object')


def py_reversed():
    keyboard.type('# reversed() # returns an inverted iterator object')


def py_round():
    keyboard.type('# round() # returns an inverted iterator object')


def py_set():
    keyboard.type('# set() # creates a Set object')


def py_setattr():
    keyboard.type('# setattr() # sets the value of the specified attribute of the specified object')


def py_slice():
    keyboard.type('# slice() # returns a slice object')


def py_sorted():
    keyboard.type('# sorted() # returns a sorted list of the specified iterable object')


def py_str():
    keyboard.type('# str() # Converts the specified value into a string')


def py_sum():
    keyboard.type('# sum() # returns a number, the sum of all elements in an iterable')


def py_super():
    keyboard.type('# super() # is used to provide access to methods and properties of a parent or sibling class')


def py_tuple():
    keyboard.type('# tuple() # creates a tuple object. Elements in a tuple cannot be modified or removed')


def py_type():
    keyboard.type('# type() # returns the type of the specified object')


def py_vars():
    keyboard.type('# vars() # returns the __dict__ attribute of an object')


def py_zip():
    keyboard.type('# zip() # returns a zip object which is an iterator of tuples where the first element in each passed iterator is paired and then the second element in each passed iterator is paired, etc.')
