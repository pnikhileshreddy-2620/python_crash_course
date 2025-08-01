
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_to_poll = ['jen', 'phil', 'nikhilesh', 'chandu', 'sarah']

for pepole in people_to_poll:
    if pepole in favorite_languages:
        print(f"Thank you, {pepole.title()}, for taking the poll!")
    else:
        print(f"{pepole.title()}, please take our favorite programming language poll!")