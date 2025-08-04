


def counting_words(filename):
    """Counting no of words in file using length function
    using split() and also using exception"""
    try:
        with open(filename) as f:
             words = f.read().lower().split()
             print(f"No of words in the file is {len(words)}")
    except FileNotFoundError:
        print(f"Sorry this file {filename} not found in this directory")

# file = 'test.txt'
# counting_words(file)

muliple_file =['test.txt','jkvnksd','dfdsf']

for  i in muliple_file:
    counting_words(i)