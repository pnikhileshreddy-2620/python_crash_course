filename ='test.txt'

try:

    with open(filename) as fr:
        concept = fr.read().lower().split()
except FileNotFoundError:
    print("File not found in the directory")
else:
    print(len(concept))
    print(concept)
    count =0
    for  i in concept:
        if i =="python":
            count +=1
    print(count)

    print(f"No of words in file {filename} is {len(concept)} ")
