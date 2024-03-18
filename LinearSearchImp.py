"""
#Linear Search Algorithm Implementation
#Date:2024/03/18
#Author:Yeswanth
"""


class LinearSearchImp:
    def __init__(self):
        self.list_of_items = [20, 2, 15, 28, 36, 41]
        self.found = False

    def search_linearly(self, key):

        for i in range(len(self.list_of_items)):
            if int(key) == self.list_of_items[i]:
                self.found = True
                break
        if self.found is True:
            print(key, "Found in List")
        else:
            print(key, "Not Found in List")


linear_search_imp = LinearSearchImp()
while True:
    key_input = input("Enter key to search: ")
    linear_search_imp.search_linearly(key_input)
