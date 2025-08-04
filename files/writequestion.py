filename ='Write.txt'
with open(filename,'w') as fp:
    fp.write("Files \n")
    fp.write("My name is Nikhilesh")

with open(filename,'r')as fr:
    print(fr.read())
