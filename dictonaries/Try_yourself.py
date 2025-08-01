person ={
    'first_name':'Nikhilesh',
    'last_name':'Reddy',
    'age':25,
    'city':'Nellore'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


fav_number= {
    'nikhilesh':1,
    'mojesh': 2,
    'thanju':3,
    'kattu':4,
    'Gangi':5
}
print(f'Nikhilesh favoritre number is {fav_number['nikhilesh']}')
print(f'Mojesh favoritre number is {fav_number['mojesh']}')
print(f'Thanju favoritre number is {fav_number['thanju']}')
print(f'Kattu favoritre number is {fav_number['kattu']}')
print(f'Gangi favoritre number is {fav_number['Gangi']}')

print("----for loop -------")
for keys,value in fav_number.items():
    print(f'{keys} favorite number is {value}')