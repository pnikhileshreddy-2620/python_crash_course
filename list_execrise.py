names =["Nikhilesh","Mojesh","Thanju","Kattu","Gangi","Harish"]

for i in names:

    print("Welcome to python dev "+i)

transportations=["NS400Z"]
print(f"I would like to own a {transportations[0]} motorcycle.")
print("-----------------NEW TASK FOR LIST------------------------------------")
print()
deceased =["Nikhilesh","Gangi","Mojesh"]
# print(len(deceased))
# del deceased[0]
# print(len(deceased))
deceased[0]="Kattu"


""""print the invitation message"""
for person in deceased:
    print("Hi "+person+" please join  us in dinner")


# Add more person to the list .And print the invitation again
""""Inserting new elements in the list"""
deceased.insert(0,"Thanju")
deceased.insert(2,"Raju")
deceased.append("Harish")


print()

""""Print the invitation after updating list"""
for person in deceased:
    print("Hi "+person+" please join  us in dinner")
print("Updated list ",deceased)
print()

""""DELETE THE ELEMENT INSIDE THE LIST"""
for person in deceased[2::]:
    print(person+" you’re sorry you can’t invite them to dinner")
    deceased.pop()

print(deceased)
print(len(deceased))
print()
""""After delete elements inside list. print the remaining element"""
for persons in deceased:
    print(persons+" you still have invited")



for del_person in range(0,len(deceased)):
    deceased.pop()

print()
print("Printing list elements ", deceased)