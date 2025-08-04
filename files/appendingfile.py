filename= 'append.txt'

with open(filename,'a') as fa:
    fa.write("I am python dev \n")
    fa.write("Having 2.5 year experience in dev ")
with open(filename,'r') as fr:
    print(fr.read())