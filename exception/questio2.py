filename ='test.txt'

try:
    with open(filename) as fr:
        concept = fr.read().split()
except FileNotFoundError:
    print("File not found in the directory")
else:
    print(len(concept))
    print(concept)