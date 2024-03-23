"""
#Author: Yeswanth
#Date: 2024/03/23
#Description: User Defined Exception Practice
"""


class ExceptionHandle3(Exception):
    def __init__(self, msg):
        self.msg = msg

    def print_userdef_exception(self):
        print("User Defined Exception", self.msg)


class UserDefinedException:
    def user_defined_ex(self, event_occured):
        try:
            if event_occured == "Accident":
                raise ExceptionHandle3("Accident Occurred")
        except ExceptionHandle3 as e:
            print(e.print_userdef_exception())
            print("Exception Handled")


user_defined_obj = UserDefinedException()
user_input_read = input("Event: ")
user_defined_obj.user_defined_ex(user_input_read)
