def make_album():
    user_album ={}
    i =True
    print("If you want to quit the code type [q]")
    while i:
        artist = input("Enter the artist name :")
        title = input("Enter the title name :")
        user_album[artist]=title
        users_input = input("Do you want to quit  ").lower()
        if users_input=='q':
            i =False
    return user_album
user_album=make_album()
print(user_album)

