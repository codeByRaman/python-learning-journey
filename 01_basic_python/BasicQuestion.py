"""
1. Print your name, age and college name.
2. Create two variables a = 20 and b = 10. Print their sum, difference, multiplication and division.
3. Create variables of type int, float, str and bool. Print their data types using type().
4. Swap two variables without using a third variable.
5. Convert the string "100" into an integer and add 50.
"""

#Answer 1 :
print("Raman Kumar")
print("My age is 20")
print("My college name is Kalinga university")

#Answer 2 :
a = 20 
b = 10

print("Sum is ", a+ b)
print("Difference is ", a - b)
print ("Multiplication is : ",a * b)
print("Division is : ", a / b)

#Answer 3 : 
num = 23
num1 = 23.45
str = "Raman Kumar"
boolean = True

print(type(num))
print(type(num1))
print(type(str))
print(type(boolean))

#Answer 4 :

number_01 = 23
number_02 = 43

#swap 
number_02 = number_02 - number_01
number_01 = number_01 + number_02
number_02 = number_01 - number_02

print("number_01 is : ",number_01 , "and number_02 is : " ,number_02)

#Answer 5 :

num_01 = int("100")
print(num_01 + 50)