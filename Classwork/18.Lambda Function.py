#Syntax of Lambda Function
#lambda arguments: expression
#Example of Lambda Function
def square(x):
    return x*x
a=int(input())
print(square(a))

square_lambda=lambda x:x*x
a=int(input())
print(square_lambda(a))
#Lambda Function with Multiple Arguments
def add(a,b):
    return a+b
a=int(input())
b=int(input())
print(add(a,b))

add_lambda=lambda a,b:a+b
a=int(input())
b=int(input())
print(add_lambda(a,b))

#Lambda Function with if-else Conditions
max_number=lambda a,b: a if a>b else b
a=int(input()) 
b=int(input()) 
print(max_number(a,b))

def max_nyumber(a,b):
    return max(a,b)
a=int(input())
b=int(input())
print(max(a,b))

def max_number(a,b):
    return a if a>b else b
print(max_number(8,7))

#Using Lambda with map(), filter(), and reduce()
a=list(map(int,input().split(',')))
squared = list(map(lambda x:x*x, a))
print(squared)

#Using filter() – Keep Only True Values
a=list(map(int,input().split(',')))
even=list(filter(lambda x:x%2==0, a))
print(even)

#Using reduce() – Reduce a List to a Single Value
from functools import reduce
a=list(map(int,input().split(',')))
sum_of_all=reduce(lambda x,y:x+y,a)
print(sum_of_all)

#Lambda Function with Lists & Sorting
students=eval(input())
sorted_students=sorted(students,key=lambda x:x[1])
print(sorted_students)

#Lambda Function in Dictionaries
gardes=eval(input())
sorted_gardes=dict(sorted(gardes.items(),key=lambda item:item[1]))
print(sorted_gardes)

#Lambda with Default Arguments
greet=lambda name=input(): f"Hello,{name}!"
print(greet("Eswar"))
print(greet())

#Lambda Inside Another Function (Nested Lambda)
def multiply_by(n):
    return lambda x: x * n
double = multiply_by(2)
triple = multiply_by(3)
a=int(input())
b=int(input())
print(double(a))
print(triple(b))





