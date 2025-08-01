""" Remove Duplicates"""

remove_duplicate=[4,1,2,5,53,98,5,45,43,4,1]

new =set(remove_duplicate)
print(list(new))


remove_duplicate=[4,1,2,5,53,98,5,45,43,4,1]
print(len(remove_duplicate))

unique_items=[]

for item in remove_duplicate:
    if item not in unique_items:
        unique_items.append(item)
print(unique_items)