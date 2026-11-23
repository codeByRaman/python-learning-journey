"""
Q1. Take a number from the user and check whether it is positive or negative.
Q2. Check whether a number is even or odd.
Q3. Take age as input. If age is 18 or above, print "Eligible to vote", otherwise print "Not eligible".
Q4. Take two numbers and print the greater number.
Q5. Check whether a number is zero or non-zero.
"""

number = int(input("Enter the number : "))
if number > 0:
    print("Number is Positive")
elif number == 0:
    print("Number is Zero")
else :
    print("Number is Negative")
    
    
#number is Odd or Even

if number % 2 == 0:
    print("Number is Even Number")
else :
    print("Number is Odd Number")


# age 
age = int(input("Enter the age of Person : "))
if age >= 18:
    print("Eligible for vote")
else :
    print("Not eligible for vote")
    
number_01 = int(input("Enter the first number : "))
number_02 = int(input("Enter the second number : "))

if (number_01 > number_02):
    print(number_01, "is Grater then ",number_02)
elif number_02 == number_01:
    print("Both are equal")
else: 
    print(number_02,"is Grater then ",number_01)
    
if (number_01 == 0):
    print("It is a Zero")
else:
    print("It is a non Zero")