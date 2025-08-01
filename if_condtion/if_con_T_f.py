from random import *

user_input = int(input("Enter the number [0-10] :"))
system_input = randint(0,10)


if user_input==system_input:
    print("=")
elif user_input>system_input:
    print("User")
elif user_input<system_input:
    print("System")
