#PYTHON CONDITIONALS & LOOPS


# Write a program that asks the user for a number and prints whether it is positive, negative, or zero
num=int(input("Enter a Number: "))
if(num<0):
    print("Negative")
elif(num>0):
    print("Positive")
else:
    print("Zero")

# Create a program that checks if a person is eligible to vote (age >= 18)
age=int(input("Enter your age: "))
if(age>=18):
    print("You are eligible to vote")
else:
    print("Not Eligible")

# Write a program that takes a number from the user and prints “Even” if it is even, otherwise “Odd”.
num=int(input("Enter a Number: ")) 
if(num%2==0):
    print("Even")
else:
    print("Odd")


# Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case .
day=int(input("Enter a day number between 1-7: "))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")


# Write a program using match case that simulates a simple calculator.
        #Ask the user for two numbers and an operation (+, -, *, /).
        #Perform the operation using match case.
num1=int(input("Enter first Number: "))     
num2=int(input("Enter Second Number: "))
operation=input("Enter (+, -, *, /) for Operation.")
match operation:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)


# Print numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)

# Print the multiplication table of a number (entered by user).   
num=int(input("Enter a number: "))
for i in range(1, 11):
    print(num*i)

# Calculate the sum of all numbers from 1 to 100 using a for loop
num=0
for i in range(1, 101):
    num=num+i
print(num)

# Print the following pattern using a for loop:
# *
# **
# ***
# ****
rows=4
for i in range(1, rows+1):
    print("*"*i)

    

# Print numbers from 1 to 10 using a while loop
i=1
while(i<11):
    print(i)
    i=i+1


 # Write a program that keeps asking the user to enter a password until they enter the correct one.
pwd=input("Please Enter Your Password: ")
while(pwd!="This"):
    pwd=input("Wrong! Please Enter Your Password Again: ")
    if(pwd=="This"):
        print("Logged In")


# Use a while loop to reverse a given number (e.g., 123 → 321).
inp=int(input("Enter a number to reverse: "))
fin=""
while(inp>0):
    temp=inp%10
    fin=(fin + str(temp))
    inp=inp//10
print(fin)



# Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break )
for i in range(1,11):
    if(i==7):
        break
    print(i)


# Print numbers from 1 to 10, skipping the number 5 (use continue ).
for i in range(1,11):
    if(i==5):
        continue
    print(i)


# Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass )
for i in range(1,6):
    if(i==3):
        pass
    print(i)