names=["Nikhiles","Kattu","Thanju","Mojesh","Raj","Gangi"]

print("First three items in the list")
for  i in names[:3]:
    print(i)

print("Three items for the middle of the list")
for i in names[int(len(names)/2):]:
    print(i)

print("Last three items in the list")
for i in names[-3:]:
    print(i)

person = ("Nikhilesh", "Engineer", "Hyderabad")
name, role, city = person
print(name)  # Output: Nikhilesh
