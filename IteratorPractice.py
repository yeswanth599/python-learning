"""
#Author: Yeswanth
#Date:2024/03/23
#Description:Iterators Practice
"""


class IteratorPractice:

    def __init__(self, data_list):
        self.data_list = data_list

    def for_loop_p(self):
        print("For Loop Output")
        for i in self.data_list:
            print(i)

    def iterator_p(self):
        print("Iterator Output")
        my_iterator = iter(self.data_list)
        print(next(my_iterator))
        print(next(my_iterator))


data_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
iterator_p_obj = IteratorPractice(data_list)
iterator_p_obj.for_loop_p()
iterator_p_obj.iterator_p()
