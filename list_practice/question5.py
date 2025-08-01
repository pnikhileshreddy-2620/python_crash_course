"""Count Occurrences"""

count_list =[1,2,3,4,3,54,6,3,1,7,9]

count_dict={}

for i in range(0,len(count_list)):
    value= count_list.count(i)
    count_dict[i]=value

print(count_dict)
