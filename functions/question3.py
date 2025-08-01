from list_practice.pratice_question import names


def greet_user(username,age,number=1):
    """passing the information in the greet_user [username will display]"""
    print(f"Hello  {username}")
    print(f"age:{age}")
    print(f"number {number}")

greet_user("Nikhilesh",25)
greet_user(age=1,username='hp',number=2)