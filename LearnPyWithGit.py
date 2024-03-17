class LearnPyWithGit:
    def __init__(self, name, address, phone_number, email_id):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email_id = email_id

    def print_user_address(self):
        print("requested user details: ")
        print(self.name)
        print(self.address)
        print(self.phone_number)
        print(self.email_id)


print("Enter User Details")
input_name = input("Enter User Name: ")
input_address = input("Enter User Address: ")
input_phone_number = input("Enter User PhoneNumbr: ")
input_email_id = input("Enter User email id: ")
learnpy_with_gitobj = LearnPyWithGit(input_name, input_address, input_phone_number, input_email_id)
learnpy_with_gitobj.print_user_address()
print("User details entered")
