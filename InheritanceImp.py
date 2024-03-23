"""
#Author: Yeswanth
#Date: 2024/03/23
#Description: Learning about Inheritance concept in Python
"""


class InheritanceImp:
    def parent_class_method(self):
        self.parent_class_variable = "Parent Class Variable"
        print(self.parent_class_variable)


class ChildClassImp(InheritanceImp):
    def child_class_method(self):
        self.child_class_variable = "Child Class Variable"
        self.parent_class_variable = "Updated Parent Class Variable"

        print(self.parent_class_variable)


child_class_obj = ChildClassImp()
child_class_obj.parent_class_method()
child_class_obj.child_class_method()
