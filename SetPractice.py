"""
#Author: Yeswanth
#Date:2024/03/26
#Description: Learning about Set & Frozen Set
"""


class SetPractice:
    def __init__(self, set_elements, frozen_set_elements):
        self.set_elements = set_elements
        self.frozen_set_elements = frozen_set_elements

    def set_elements_f(self):
        new_set = set(self.set_elements)
        new_set.add("5")
        new_set.add("2")
        new_set.remove("3")
        for i in new_set:
            print(i)

    def frozen_set_eleme(self):
        new_frozen_set = frozenset(self.frozen_set_elements)
        print("frozen set elements are:")
        for i in new_frozen_set:
            print(i)


set_elements_data_sending = {"1", "2", "3", "4"}
frozen_set_elements_data = frozenset(set_elements_data_sending)

set_practice_obj = SetPractice(set_elements_data_sending, frozen_set_elements_data)
set_practice_obj.set_elements_f()
set_practice_obj.frozen_set_eleme()