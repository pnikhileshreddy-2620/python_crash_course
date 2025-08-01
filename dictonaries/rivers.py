#The Nile runs through Egypt
from ast import Param

rivers ={

    'Nile':'Egypt',
    'Amazon':'Colombia',
    'Yangtze':'China',
    'Mississippi':'USA',
    'Ganges':'India'
}

for k,v in rivers.items():
    print(f"The {k} runs through {v} ")

print("------------------------------")
for k in rivers.keys():
    print(f"Name of the river :{k}")
print("------------------------------")

for v in rivers.values():
    print(f"Country :{v}")