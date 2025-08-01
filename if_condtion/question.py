alien_color =['green', 'yellow',  'red']

for alien in alien_color:
    if alien=='green':
        print(" just earned 5 points")
    elif alien=='yellow':
        print("just earned 10 points")
    elif alien=='red':
        print('just earned 15 points')
print("-------------------------")
ages =[1,2,3,19,21,65,55,43,35]

for i in  ages:
    if 0<i<2:
        print("Baby",i)
    elif 2<=i<4:
        print('toddler',i)
    elif 4<=i<13:
        print('kid',i)
    elif 13<=i<20:
        print('teenager',i)
    elif 20<=i<60:
        print('adult',i)
    else:
        print('elder',i)