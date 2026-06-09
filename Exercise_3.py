# PYTHON STRINGS

# Create a string variable name with your full name. Print:
    # The first character
    # The last character
    # The length of the string
name="Avneesh Kumar"
print(name[0])
print(name[-1])
print(len(name))


# Concatenate two strings: "Hello" and "World" with a space in between
str1="Hello"
str2="World"
complete=(str1+ " " +str2)
print(complete)



# Given text = "Python Programming" , do the following:
    # Print the first 6 characters
    # Print the last 6 characters
    # Print every second character from the string
text="Python Programming"
print(text[0:7])
print(text[-6:])
print(text[0::2])


# Reverse the string text using slicing
text="Python Programming"
print(text[::-1])


# Take the string " i love python programming " and:
    # Remove extra spaces from both ends
    # Convert it to title case
    # Count how many times "o" appears
str1=" i love python programming "
print(str1.strip())
print(str1.title())
print(str1.count("o"))


# Check if the string "123abc" is alphanumeric
str1="123abc"
print(str1.isalnum())


# Using format() , create a sentence:
    # "My name is John and I am 25 years old."
    # by passing "John" and 25 as variables
name="John"
age=25
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")


# Given sentence = "Coding in Python is fun" , replace "fun" with "awesome" and print it.
sentence = "Coding in Python is fun"
print(sentence.replace("fun", "awesome"))

sentence = "Coding in Python is fun"
print(sentence.find("Python"))

sentence = "Coding in Python is fun"
print(sentence.upper())

# Take a user input string and check if it is a palindrome (same forwards and backwards)
inp=input("Enter a String: ")
check=inp[::-1]
if(inp==check):
    print("palindrome")
else:
    print("Not a palindrome")


# Write a program that counts how many vowels are in a given string
sentence = "Coding in Python is fun"
sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in sentence.lower():
    if(char in vowels):
        sum+=1
print(f"Total vowels in the sentence are: {sum}")




