"""Common Elements"""

list1= [1,2,3,4,5]
list2 =[5,6,7,4,9]

def compare_list(list1, list2):
    if len(list1)!=len(list2):
        return "Please match size of the list"
    else:
        for i in range(0,len(list1)):
            for j in range(0,len(list2)):
                if list1[i]==list2[j]:
                    common=[]
                    common.append(list1[i])
                    print(common)
                    return list1[i]

print(compare_list(list1,list2))

print(set(list1) & set(list2))