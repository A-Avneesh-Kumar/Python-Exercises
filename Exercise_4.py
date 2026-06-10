
# Python Functions & Modules

'''
# Write a function greet() that prints "Hello, Python Learner!" when called.
def greet():
    print("Hello, Python Learner!")
greet()


# Write a function square(num) that returns the square of a given number. Test it with different numbers.
def square(num):
    return num*num
print(square(12))


# Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".
def full_name(first, last):
    return (first+" "+last)
print(full_name("Amit", "Singh"))


# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
    # Both length and width
    # Only length (use default width)
def calculate_area(length, width=10):
    return (length*width)
print(calculate_area(20))
print(calculate_area(20, 20))


# Write a lambda function that adds two numbers and test it
sum = lambda x, y: x+y
print(sum(2, 4))


# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares
nums=[1, 2, 3, 4, 5]
square=list(map(lambda x:x*x, nums))
print(square)


# Write a recursive function factorial(n) that returns the factorial of a number.
def factorial(n):
    fact=n
    if(n==1):
        return 1
    elif(n<0):
        return ("please enter valid number")
    else:
        while(n>1):
            return fact + factorial(n-1)        
print(factorial(5))


# Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.
def sum_of_digits(n):
    sum=0
    n=str(n)
    for char in n:
        sum = sum + int(char)
    return sum
print(sum_of_digits(3745))


# Import the math module and use it to:
    # Find the square root of 144
    # Calculate sin(90°) (hint: use math.radians() )
import math
print(math.sqrt(144))
print(math.radians(90))


# Install and import the requests module (if available) and use it to fetch data from "https://api.github.com" 
import requests
response = requests.get("https://api.github.com")
print(response.text)


# Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls
def increment():
    local=0
    local+=1
    print(local)
    return local
print(increment())


# Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring
def multiply(a, b):
    """This is used to multiply two numbers"""
    return a*b
print(multiply.__doc__)
print(multiply(2, 9))

'''