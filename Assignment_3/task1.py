#Assignment: 3
#Module 4 : Functions & Modules in Python

#Task 1: Calculate Factorial Using a Function

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)

num = int(input("Enter a number : "))
if num == 0 :
    print("please enter a valid number")
else:
    result = factorial(num)
    print(f"factorial of number {num} is:",result)
