class User:
    def __init__(self, first_name,last_name=''):
        self.first_name =first_name
        self.last_name = last_name
        self.login=0

    def describe_user(self):
        print("User Information")
        print(f" full name of the user :{self.first_name} {self.last_name}.")
    def greet_user(self):
        print(f"Hello {self.first_name}")

    def reset_zero(self):
        self.login = 0
    def login_attempts(self, firstname,lastname):
        if self.first_name == firstname  and self.last_name==lastname:
            return 1
        else:
            self.login+=1
            if self.login==3:
                print(" Please reset the password and try again after sometime.")
                return  self.login
            else:
                return "Something want wrong"






my_user = User("Nikhilesh","ponguluru")
while True:
    first_name = input("Enter the first of the user :")
    second_name = input("Enter the last name of the user :")
    output =my_user.login_attempts(first_name,second_name)
    if output ==1:
        break
    elif output ==3:
        my_user.reset_zero()
        break


print(my_user.login)