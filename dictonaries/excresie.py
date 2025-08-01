

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}
person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

person2 = {
    'first_name': 'Alice',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles'
}

person3 = {
    'first_name': 'Bob',
    'last_name': 'Brown',
    'age': 40,
    'city': 'Chicago'
}

people = [person1, person2, person3]



for i in people:
    print("\n Information about the person")
    for k,v in i.items():
        print(f"{k.title()  :}'  ' {v}")