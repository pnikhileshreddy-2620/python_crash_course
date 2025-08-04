
print("Given me two number i wll divide for you")
print("for quit the program press q")

while True:
    first_number = input("Enter the number :")
    if first_number == 'q':
        break
    second_number   = input("Enter the number :")
    if second_number =='q':
        break
    try:

        total = int(first_number)/int(second_number)

    except ZeroDivisionError:
        print("ZERO DIVISION ERROR")
    else:
        print(total)