'''
#1. Add Two Numbers
def add(a,b):
    return a+b
x=int(input())
y=int(input())
print(add(x,y))

#2. Square a Number
def square(a):
    return a*a
x=int(input())
print(square(x))

#3. Area of a Circle
import math
def area_of_circle(a):
    return math.pi*a**2         # we use also pi = 3.141*a**2
x=int(input())
print(area_of_circle(x))

#4. Greet the User
def greet(a):
    return f"Hello {a}!"
x=input()
print(greet(x))

#5. Convert Celsius to Fahrenheit
def convert(a):
    return (9/5*a)+32
x=int(input())
print(convert(x))

#6. Multiply Three Numbers
def multiply_three_numbers(a,b,c):
    return a*b*c
x=int(input())
y=int(input())
z=int(input())
print(multiply_three_numbers(x,y,z))

#7. Calculate Simple Interest
def simple_interest(prinple,rate,time):
    return (prinple*rate*time)/100
a=int(input())
b=int(input())
c=int(input())
print(simple_interest(a,b,c))

#8. Find Length of a String
def count_string(a):
    return len(a)
x=input()
print(count_string(x))

#9. Append to a List
def append_list(a,b):
    a.append(b)
    return a
x=list(map(int,input().split()))
y=int(input())
result=append_list(x,y)
print(result)

#10. Double Each Element in a List
def element(a):
    return [x*2 for x in a]
x=list(map(int,input().split()))
print(element(x))

#11. Sort a List
def sort(a):
    return sorted(a)
x=list(map(int,input().split(',')))
print(sort(x))

#12. Clear a List Inside Function
def clear_list(a):
    return a.clear()
x=list(map(int,input().split()))
print(clear_list(x),"cleard list")

#13. Update Dictionary Value
def dict_update(d,key,new_value):
    d[key]=new_value
    return d
    
d = eval(input("Enter dictionary: "))
key = input("Enter key to update: ")
new_value = input("Enter new value: ")

if new_value.isdigit():
    new_value = int(new_value)

print(dict_update(d,key,new_value))

#14. Remove Element from List by Value
def remove_element(a,b):
    a.remove(b)
    return a
a=list(map(int,input().split(',')))
b=int(input())
print(remove_element(a,b))

#15. Add Key to Dictionary
def dict_update(d,key,new_value):
    d[key]=new_value
    return d
    
d = eval(input("Enter dictionary: "))
key = input("Enter key to update: ")
new_value = input("Enter new value: ")

if new_value.isdigit():
    new_value = int(new_value)

print(dict_update(d,key,new_value))

#16. Increment All Values in Dictionary
def increment_values(a):
    for k in a:
        if isinstance(a[k], (int, float)):
            a[k]+=1
    return a
d = eval(input("Enter dictionary: "))
print("Updated dictionary:", increment_values(d))

#17. Factorial of a Number
def factorial(a):
    if a==0 or a==1:
        return 1
    else:
        return a*factorial(a-1)
a=int(input())
print(factorial(a))

#18. Fibonacci Number (Nth Term)
def fibonacci(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    else:
        a,b=0,1
        for i in range(2,n+1):
            a,b=b,a+b
        return b
x=int(input())
print(fibonacci(x))

#19. Sum of First N Natural Numbers
def sum_of_natural_numbers(num):
    total=0
    for i in range(1,num+1):
        total+=i
    return total
a=int(input())
print(sum_of_natural_numbers(a))

#20. Reverse a String Using Recursion
def reverse_string(a):
    return a[::-1]
x=input("Enter a string: ")
print(f"Reversed string is:",reverse_string(x))
                #(or)
def reverse_string(s):
    # Base case: if string has 0 or 1 character
    if len(s) <= 1:
        return s
    else:
        # Take last char + reverse of rest
        return s[-1] + reverse_string(s[:-1])
text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))

#21. Power of a Number (a^b using recursion)
def power_of_number(a,b):
    return a**b
x=int(input("Enter a num1: "))
y=int(input("Enter a num2: "))
print("Result is",power_of_number(x,y))
           #(or)
def power_of_number(a,b):
    if b==0:
        return 1
    else:
        return a*power_of_number(a,b-1)
x=int(input("Enter a num1: "))
y=int(input("Enter a num2: "))
print(f"{x}^{y} Result is",power_of_number(x,y))

#22. Sum of Digits Using Recursion
def sum_of_digits(n):

    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)
    
num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
'''