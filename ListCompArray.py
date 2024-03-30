"""
#Author:Yeswanth
#Date:2024/03/28
#Description: Array Operations for List comprehensions
"""
def addition_of_array():
    a = [[10, 20], [30, 40],[70,80]]
    b = [[20, 30], [40, 50],[50,60]]
    x = [a[i][j]*b[i][j] for i in range(0, len(a)) for j in range(0,len(b[0]))]
    print(len(a))
    print(len(b))
    print(x)


addition_of_array()
