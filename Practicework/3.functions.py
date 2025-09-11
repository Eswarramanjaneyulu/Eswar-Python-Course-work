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
'''
