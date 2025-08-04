

filepath = 'C:/Users/pongredd/Downloads/customer.txt'
with open(filepath) as file_object:
    lines = file_object.readlines()
   

for line in lines:
    print(line,end='')
