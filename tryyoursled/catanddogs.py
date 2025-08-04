
def func(function):
    try:
        with open(function) as f1:
            content = f1.read()
            print(content)
    except FileNotFoundError:
        pass



all =['Cat.txt','dog.txt','nikki.txt']

for i in all:
    func(i)
