def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and the message printed on it is: '{message}'.")

# Making a large shirt with the default message
make_shirt()

# Making a medium shirt with the default message
make_shirt(size="Medium")

# Making a custom shirt with a different message
make_shirt(size="Small", message="Code. Debug. Repeat.")
