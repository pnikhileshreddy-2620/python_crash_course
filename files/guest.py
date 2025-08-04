guest = 'guest.txt'

while True:
    user = input("Enter the name of the user (or type 'exit' to stop): ")
    if user.lower() == 'exit':
        break
    with open(guest, "a") as gw:
        gw.write(user + "\n")

with open(guest,'r') as gr:
    print("Name of the user :",gr.readlines())