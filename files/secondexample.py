
filepath = 'C:/Users/pongredd/Downloads/customer.txt'
with open(filepath) as file_object:
    lines = file_object.readlines()

new_String=''
for line in lines:
    new_String +=line.rstrip()

print(new_String)
print(len(new_String))