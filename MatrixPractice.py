"""
#Author:Yeswanth
#Date:2024/03/28
#Description: Matrix practice for Python
"""

import numpy as np


class MatrixPractice:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

    def addition_two_matrices_np(self):
        print("Length of Array: ", len(self.array1))
        print("Length of Array[0]: ", len(self.array1[0]))
        print("range of Array", self.array1)
        print("range of length of array1", len(self.array1))
        result = np.array(self.array1) + np.array(self.array2)
        print("")
        print("Adding of Two Array`s using Numpy Module")
        print(result)

    def addition_two_numbers_for(self):
        print("Adding of Two Array`s using for")
        result = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        for i in range(len(self.array1)):

            for j in range(len(self.array1[0])):
                result[i][j] = self.array1[i][j] + self.array2[i][j]
        for z in range(len(result)):
            print(result[z])


input_array1 = [[1, 2, 3],
                [3, 4, 5],
                [5, 6, 7]]
input_array2 = [[4, 5, 6],
                [5, 6, 7],
                [1, 2, 3]]

matrix_practice_obj = MatrixPractice(input_array1, input_array2)
matrix_practice_obj.addition_two_matrices_np()
matrix_practice_obj.addition_two_numbers_for()
