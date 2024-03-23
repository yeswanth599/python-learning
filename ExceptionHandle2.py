class ExceptionHandle2:

    def __init__(self):
        self.memory_size = 0

    def memory_error_verification(self, memory_size_latest):
        self.memory_size = memory_size_latest
        try:
            if memory_size_latest > 200:
                raise MemoryError("Memory Size increased")
        except MemoryError:
            print("Memory Exception occurred, Handled")
        finally:
            print("finally Block Entered")


exception_handle_2 = ExceptionHandle2()

read_input = input("Enter Current Memory Size: ")
exception_handle_2.memory_error_verification(int(read_input))
