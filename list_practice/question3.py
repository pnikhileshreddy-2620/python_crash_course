""""- Reverse a List"""

rev_list =[]

for i in range(10,0,-1):
    rev_list.append(i)

print(rev_list)
rev_list.reverse()
print(rev_list)

rev_list.clear()
for i in range(10,0,-1):
    rev_list.append(i)
for k in rev_list[::-1]:
    print(k, end=" ")