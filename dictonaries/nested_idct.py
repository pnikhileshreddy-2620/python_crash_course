
users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 }
}
print(users['aeinstein']['first'])


for username, userinfo in users.items():
    print("\n username:"+username)
    fullname=userinfo['first']+userinfo['last']
    location_user= userinfo['location']
    print(fullname)
    print(location_user)