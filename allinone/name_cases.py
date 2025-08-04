name ="Eric"
print('"hello '.title() +name+"," +'would you like to learn some Python today?”',)
print("Upper case",name.upper())
print("lower case",name.lower())
print("Title ",name.title())

famous_quote ='Albert Einstein "once said,'
quote = '“A person who never made a\t\n mistake never tried anything new.”'

print(famous_quote+quote)

famous_person=famous_quote+quote
print(famous_person)

my_name = " nikhilesh  reddy "
print("rstrip :",my_name.rstrip())
print("lstrip :",my_name.lstrip())
print("strip  :",my_name.strip())


count_string ="banana"
print(count_string.count("a"))

print(count_string.startswith("b") and count_string.endswith("a"))

input_string_test ="This is a test. This is only a test."

input_string_test=input_string_test.replace("test","sample")
print(input_string_test)

alphanumeric = "python123"
print(alphanumeric.isalnum())


palindrome= "racecar"
print("palindrome checker :",palindrome==palindrome[::-1])

vowels_remove = "Programming is awesome!"
print(vowels_remove)
vowels = {'a', 'e', 'i', 'o', 'u'}
result = "".join(chars for chars in vowels_remove if chars not  in vowels)

print("removing the vowels :",result)




