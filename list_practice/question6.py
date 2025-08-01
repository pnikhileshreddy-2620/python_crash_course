li =[1,2,3,4]

def roate(list,k):
    n= len(list)
    if n==0:
        return []
    k % n
    return list[k:]+list[:k]

print(roate(li,2))
