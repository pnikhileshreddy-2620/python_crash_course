polling_active= True
response ={}

while polling_active:
    key = input("What is your name :")
    value = int(input("What you age :"))

    response[key]=value

    repeat = input("cloud you want to provide the access to next person [yes/No] ").lower()
    if repeat=='no':
        polling_active=False

for i , k in response.items():
    print(i,k)

