import  json
numbers= [ i for i in range(0,6)]
filename  = 'numberjson.json'
with open(filename,'w') as fw:
    json.dump(numbers,fw)


with open(filename) as fn:
    number = json.load(fn)

print(number)

