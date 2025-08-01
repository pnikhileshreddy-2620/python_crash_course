alien=[]

for alien_auto in range(30):
    new_aline={'color':'Green','point':5,'speed':'slow','number':alien_auto}
    alien.append(new_aline)
i=0
for aliens in alien[5:]:
    print(i, aliens)
    i+=1