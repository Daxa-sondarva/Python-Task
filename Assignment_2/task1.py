#Assignment 2
#Module 3 :Control Structure in Python

# Task 1 :  Check if Number is Even or Odd

#Get input from user & convert into intger using typecasting -->use int() function to type cast
num = int(input("Enter a Number : "))

#check the number is divisible with 2 or not using if statement if statement true it is even if not it is odd number
if num % 2 == 0:
    print(f"{num} is an Even Number.")
else:
    print(f"{num} is an Odd Number.")
