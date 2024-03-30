"""
#Author:Yeswanth
#Date:2024/03/30
#Description:List comprehensions
"""


def x_conditions(x):
    if x < 5:
        return x * x * x
    else:
        return x * x


def print_list_comp():
    x = [x_conditions(x) for x in range(1, 10)]
    print(x)


print_list_comp()
