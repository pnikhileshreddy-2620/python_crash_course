

greeting= ['Nikhilesh','Kattu','Mojesh','Thanju','Gangi','admin']

for user_names in greeting[:]:
    if 0==len(user_names):
        print("We need to find some users!")
    elif  user_names=='admin':
        print(f'Hello {user_names}, would you like to see a status report?')
        greeting.remove(user_names)

    else:
        print(f'Hello {user_names}, thank you for logging in again')
        greeting.remove(user_names)


print(greeting)
