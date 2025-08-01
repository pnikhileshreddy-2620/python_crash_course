""""- Sum of List Elements"""
total_sum_of_list =[10,33,22,45,98,88]

print(sum(total_sum_of_list))

total =0

for i  in total_sum_of_list:
    total +=i
print(total)


def total_sum_function(list):
    total =0
    for i in list:
        total +=i

    return total

print(total_sum_function(total_sum_of_list))

""""Same things did it in three ways"""