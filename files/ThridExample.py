print("====READING==========")
with open('learning_python.txt') as lp:
    
    content = lp.read()
    print(content)
print('======UISNG==========')
with open('learning_python.txt') as file:

    for line in file:
        print(line.strip())
print("\n=== Working with lines stored in a list ===")
with open('learning_python.txt') as file:
    lines = file.readlines()


for line in lines:
    print(line.strip())
