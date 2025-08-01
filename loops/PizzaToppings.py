
print("To the Exit please type quit")
active= True
topping=[]
while active:
    userinput= input("Enter the topping ")

    if userinput=='quit':
        break
    else:
        topping.append(userinput)
print(topping)