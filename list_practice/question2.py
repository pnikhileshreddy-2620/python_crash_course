""""- Find the Maximum Value"""

max_value_in_list=[1,55,3,22,56,98,55]

print(max(max_value_in_list))

max_value_in_list.sort()
print(max_value_in_list[-1])


def max_value(list):
    return  max(list)

print(max_value(max_value_in_list))


max_value_in_list=[1,55,3,22,56,98,55]


for i in range(0,len(max_value_in_list)-1):
    if max_value_in_list[i]>=max_value_in_list[i+1]:
        temp =max_value_in_list[i+1]
        max_value_in_list[i+1] =max_value_in_list[i]
        max_value_in_list[i]=temp

print(max_value_in_list)


