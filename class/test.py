class User:
    def __init__(self, first_name, last_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("\n📋 User Information")
        print(f"👤 Full Name: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"\n👋 Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def login(self, input_firstname, input_lastname):
        if self.first_name.lower() == input_firstname.lower() and self.last_name.lower() == input_lastname.lower():
            print("✅ Login successful!")
            return True
        else:
            self.increment_login_attempts()
            if self.login_attempts >= 3:
                print("❌ Too many failed attempts. Please reset your password.")
            else:
                print("⚠️ Incorrect credentials. Try again.")
            return False

# Create a user instance
my_user = User("Nikhilesh", "Ponguluru")

# Simulate login attempts
while True:
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    if my_user.login(first_name, last_name):
        break
    if my_user.login_attempts >= 3:
        my_user.reset_login_attempts()
        break

print(f"\n🔢 Login attempts: {my_user.login_attempts}")

# Demonstrate increment and reset methods
print("\n📈 Testing increment_login_attempts:")
for _ in range(5):
    my_user.increment_login_attempts()
print(f"Login attempts after incrementing: {my_user.login_attempts}")

print("\n🔄 Testing reset_login_attempts:")
my_user.reset_login_attempts()
print(f"Login attempts after reset: {my_user.login_attempts}")