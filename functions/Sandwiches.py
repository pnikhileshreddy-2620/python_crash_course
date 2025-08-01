'''Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the
sandwich that is being ordered. Call the function three times, using a different
number of arguments each time.'''

def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

# Call the function three times with different numbers of arguments
make_sandwich('cheese', 'lettuce', 'tomato')
make_sandwich('turkey', 'mayo')
make_sandwich('peanut butter', 'jelly', 'banana', 'honey')
