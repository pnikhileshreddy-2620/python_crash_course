import json



username  = input("What is your name :")
create_newfile  ='new_file.txt'
with open(create_newfile,'w') as nf:
    json.dump(username,nf)
    print("We'll remember you when you come back, " + username + "!")

with open(create_newfile) as rf:
    display = json.load(rf)
    print(f"Welcome back {display}")
