import time
from pynput.keyboard import Key, Controller, Listener
import re

from GUI.testsub import create_and_show_gui
from deepLearning.chat import get_trained_model
import pyautogui

from speech_record import from_microphone

import openai

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
    # if debug is True:
    #     print(" Time to Sleep 10 sec then work!!")
    #     time.sleep(10)
    print(param)

    status, text = get_trained_model("deepLearning\\TrainedModels\\mouse_move.pth",
                                     'deepLearning\\jsonFiles\\mouse_move.json', param)

    if text == "right_mouse":
        pyautogui.click(button='right')
        return
    if text == "left_mouse":
        pyautogui.click(button='left')
        return

    leave = True
    match = re.search(r'\d+', param)
    while leave:

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
                else:
                    create_and_show_gui('no direction was given\n\nsay it again', 2000)
                    voice_to_text = from_microphone()
                    status, text = get_trained_model("deepLearning\\TrainedModels\\mouse_move.pth",
                                                     'deepLearning\\jsonFiles\\mouse_move.json', voice_to_text)
                    leave = True
            except:
                print("out off move")


        else:
            create_and_show_gui('number not found\n\nsay it again', 2000)
            print("number not found")
            print("say it again")
            voice_to_text = from_microphone()

            match = re.search(r'\d+', voice_to_text)


def py_abs(param=None):
    keyboard.type('# abs() # Returns the absolute value of the specified number.\n')


def py_all(param=None):
    keyboard.type('# all() # returns True if all elements in an iterable are true, otherwise it returns False.\n')


def py_any(param=None):
    keyboard.type('# any() # returns True if all elements in an iterable are true, otherwise it returns False\n')


def py_ascii(param=None):
    keyboard.type('# ascii() # returns a readable version of any object (strings, tuples, lists, etc.)\n')


def py_bin(param=None):
    keyboard.type('# bin() # returns the binary version of an integer\n')


def py_bool(param=None):
    keyboard.type('# bool() # returns the boolean value of a specified object\n')


def py_bytearray(param=None):
    keyboard.type('# bytearray() # returns a byte array object\n')


def py_bytes(param=None):
    keyboard.type('# bytes() # returns a bytes object\n')


def py_callable(param=None):
    keyboard.type('# callable() # returns True if the specified object is callable, otherwise it returns False\n')


def py_chr(param=None):
    keyboard.type('# chr() # returns True if the specified object is callable, otherwise it returns False\n')


def py_compile(param=None):
    keyboard.type('# compile() # Returns the specified source as a code object, ready for execution\n')


def py_complex(param=None):
    keyboard.type('# complex() # returns a complex number by specifying a real number and an imaginary number\n')


def py_delattr(param=None):
    keyboard.type('# delattr() # eletes the specified attribute from the specified object\n')


def py_dict(param=None):
    keyboard.type('# dict() # creates a dictionary (array)\n')


def py_divmod(param=None):
    keyboard.type('# divmod() # returns a tuple containing the quotient and the remainder when dividing dividend by divisor')


def py_enumerate(param=None):
    keyboard.type('# enumerate() # returns a tuple containing the quotient and the remainder when dividing dividend by divisor')


def py_eval(param=None):
    keyboard.type('# eval() # evaluates the given expression, if it is a legal Python statement')


def py_exec(param=None):
    keyboard.type('# exec() # executes the specified Python code')


def py_filter(param=None):
    keyboard.type('# filter() # returns an iterator in which the elements are filtered by a function to check whether the element is accepted or not')


def py_float(param=None):
    keyboard.type('# float() # Converts the specified value to a floating point number')


def py_format(param=None):
    keyboard.type('# format() # formats a specified value into a specific format')


def py_frozenset(param=None):
    keyboard.type('# frozenset() # returns an immutable frozenset object')


def py_getattr(param=None):
    keyboard.type('# getattr() # returns the value of the specified attribute from the specified object')


def py_globals(param=None):
    keyboard.type('# globals() # returns the global symbol table as a dictionary')


def py_hasattr(param=None):
    keyboard.type('# hasattr() # returns True if the specified object has the specified attribute, otherwise False')


def py_hex(param=None):
    keyboard.type('# hex() # converts the specified number to a hexadecimal value')


def py_id(param=None):
    keyboard.type('# id() # returns a unique ID for the specified object')


def py_input(param=None):
    keyboard.type('# input() # returns a unique ID for the specified object')


def py_int(param=None):
    keyboard.type('# int() # Converts the specified value into an integer number')


def py_isinstance(param=None):
    keyboard.type('# isinstance() # returns True if the specified object is of the specified type, otherwise False')


def py_issubclass(param=None):
    keyboard.type('# issubclass() # returns True if the specified object is a subclass of the specified object, otherwise False')


def py_iter(param=None):
    keyboard.type('# iter() # returns an iterator object')


def py_len(param=None):
    keyboard.type('# len() # returns the number of elements in an object')


def py_list(param=None):
    keyboard.type('# list() # creates a list object')


def py_locals(param=None):
    keyboard.type('# locals() # returns the local symbol table as a dictionary')


def py_map(param=None):
    keyboard.type('# map() # executes a specified function for each element in an iterable')


def py_max(param=None):
    keyboard.type('# max() # returns the element with the highest value or the element with the highest value in an iterable')


def py_memoryview(param=None):
    keyboard.type('# memoryview() # returns a memory view object from a specified object')


def py_min(param=None):
    keyboard.type('# min() # returns the element with the lowest value or the element with the lowest value in an iterable')


def py_next(param=None):
    keyboard.type('# next() # returns the next element in an iterator')


def py_object(param=None):
    keyboard.type('# object() # returns an empty object')


def py_open(param=None):
    keyboard.type('# open() # opens a file and returns it as a file object')


def py_ord(param=None):
    keyboard.type('# ord() # returns the number representing the Unicode code of a specified character')


def py_pow(param=None):
    keyboard.type('# pow() # returns the value of x as a power of y (x^y)')


def py_print(param=None):
    keyboard.type('# print() # outputs the specified message to the screen or other standard output device')


def py_range(param=None):
    keyboard.type('# range() # returns a sequence of numbers that by default starts at 0, increments by 1, and stops before a specified number')


def py_repr(param=None):
    keyboard.type('# range() # Returns a readable version of an object')


def py_reversed(param=None):
    keyboard.type('# reversed() # returns an inverted iterator object')


def py_round(param=None):
    keyboard.type('# round() # returns an inverted iterator object')


def py_set(param=None):
    keyboard.type('# set() # creates a Set object')


def py_setattr(param=None):
    keyboard.type('# setattr() # sets the value of the specified attribute of the specified object')


def py_slice(param=None):
    keyboard.type('# slice() # returns a slice object')


def py_sorted(param=None):
    keyboard.type('# sorted() # returns a sorted list of the specified iterable object')


def py_str(param=None):
    keyboard.type('# str() # Converts the specified value into a string')


def py_sum(param=None):
    keyboard.type('# sum() # returns a number, the sum of all elements in an iterable')


def py_super(param=None):
    keyboard.type('# super() # is used to provide access to methods and properties of a parent or sibling class')


def py_tuple(param=None):
    keyboard.type('# tuple() # creates a tuple object. Elements in a tuple cannot be modified or removed')


def py_type(param=None):
    keyboard.type('# type() # returns the type of the specified object')


def py_vars(param=None):
    keyboard.type('# vars() # returns the __dict__ attribute of an object')


def py_zip(param=None):
    keyboard.type('# zip() # returns a zip object which is an iterator of tuples where the first element in each passed iterator is paired and then the second element in each passed iterator is paired, etc.')



# Stellen Sie sicher, dass Sie Ihren API-Schlüssel von OpenAI eingetragen haben
openai.api_key = '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'


def ask_gpt(param=None):
    create_and_show_gui('Ask your question to chatGPT?\n', 2000)
    voice_to_text = from_microphone()
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": voice_to_text},
        ]
    )
    print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']

# Frage an GPT-4 senden
# print(ask_gpt("Wie ist das Wetter heute?"))