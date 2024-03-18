"""
#Binary Search Algorithm Implementation
#Date:2024/03/18
#Author:Yeswanth
"""


class BinarySearchImp:
    def __init__(self):
        self.list_of_items = [20, 2, 15, 17,28, 36, 41, 55]
        self.found = False

    def search_binary(self, key):
        self.list_of_items.sort()
        low = 0
        high = len(self.list_of_items) - 1

        while low <= high and not self.found:
            mid = (low + high) // 2
            if int(key) == self.list_of_items[mid]:
                self.found = True
                break
            elif int(key) > self.list_of_items[mid]:
                low = mid + 1
            else:
                high = mid - 1
        if self.found is True:
            print(key, "Found in List")
        else:
            print(key, "Not Found in List")


binary_search_imp = BinarySearchImp()
while True:
    key_input = input("Enter key to search: ")
    binary_search_imp.search_binary(key_input)
