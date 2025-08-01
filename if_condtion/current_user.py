current_users = ['Nikhilesh', 'Kattu', 'Mojesh', 'Thanju', 'username', 'hp', 'dell']
new_users = ['HI', 'Kattu', 'kattu', 'Mojesh', 'Hp', 'hp']

# Convert current usernames to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' has already been used. Please choose a different one.")
    else:
        print(f"Username '{new_user}' is available.")
