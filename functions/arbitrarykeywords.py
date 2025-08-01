def bulid_profile(first,last, **userInfo):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for k,v in userInfo.items():
        profile[k]=v
    return profile
user = bulid_profile('Nikhilesh', 'reddy', location='Nellore')

print(user)