#Recursive Functions
#Example 1: Factorial of a Number
def factorial_number(n):
    if n==0 or n==1:
        return 1
    else:
        a= n*factorial_number(n-1)
        return a
num=int(input())
print(factorial_number(num))