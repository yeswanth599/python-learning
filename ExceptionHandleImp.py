"""
#Author: Yeswanth
#Date : 2024/03/23
#Description: This class in learning practice for Exception Handling
"""


class ExceptionHandleImp:
    def __init__(self):
        print("Exception Handling main class")

    def exception_practice(self, a, b):
        try:
            print("Exception Try block entered")
            c = a / b
            print("Exception Try block entered #1")
        except IOError:
            print("Exception occurred, Handled")


exception_obj = ExceptionHandleImp()
exception_obj.exception_practice(20, 0)
