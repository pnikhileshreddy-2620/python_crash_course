usersnames=["Nikki","Kattu","Mojesh","Thanju","Gangi"]

print("New user name register:")
user_name= input("Enter the username :")

if user_name.title() in usersnames:
    print("Please try another username , Already taken")
else:
    print(usersnames.append(user_name))
    print("Username  created")
print(usersnames)


car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')