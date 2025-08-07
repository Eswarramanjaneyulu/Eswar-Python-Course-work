#Recursive Functions
'''
a=int(input("Enter a number: "))
f=1
for i in range(1,a+1):
    f*=i
print(f)

def factorial(a):
    if a==0 or a==1:
        return 1
    else:
        return a*factorial(a-1)

a=int(input())
print(factorial(a))

#Example 2: Fibonacci Series
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))

#Example 3: Sum of Natural Numbers
def sum_natural(a):
    if a==1:
        return 1
    else:
        return a+sum_natural(a-1)
a=int(input())
print(sum_natural(a))    
'''
#Pass by Value and Pass by Reference
def value(a):
    a+=b
    print(a)
a=5
b=int(input())
value(a)
print(a)
    








