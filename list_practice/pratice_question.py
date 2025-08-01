location=["Taj Mahal","Golden Temple","Varanasi","Goa","Jaipur"]
names =["Nikhilesh","Mojesh","Thanju","Kattu","Gangi"]
print("Original list :",location)
print(sorted(location))
print("After sorting also my list is still original",location)
print("Printing sorted value in reverse",sorted(location,reverse=True))
print("After sorting also my list is still original",location)

print("-------------------------------------------")
location.reverse()
print("Reverse",location)
location.reverse()
print("Reverse",location)
location.sort()
print("Sort",location)
location.sort(reverse=True)
print("Sort",location)
print("----------------------------------------------------")
for i in range(0, len(location)):
    print("Hi "+names[i]+" you have been  invited here "+location[i])