#Factorial of a Number by using Recursive Functions
def fac(num):
    if num == 0:
        return 1
    else:
        return num*fac(num-1)
a=int(input("Enter a number: "))    
print(fac(a)) 

#Fibonacci Series Recursive Functions
def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-1)+fib(num-2)
a=int(input("Enter a number: "))
print(fib(a))

# Sum of Natural Numbers Recursive Functions
def sum_natural(num):
    if num==1:
        return 1
    else:
        return num+sum_natural(num-1)
a=int(input("Enter a number: "))
print(sum_natural(a))

#Pass by Value and Pass by Reference
#Example: Pass by Value (Immutable Objects)
def modify_value(num):
    num+=10
    print("Inside function:",num)
x=10
modify_value(x)
print("Outside function:",x)

#Example: Pass by Reference (Mutable Objects)
def modify_list(lst):
    a=int(input("Enter a Adding number:"))
    lst.append(a)
numbers=list(map(int,input().split(',')))
modify_list(numbers)
print(numbers)

#How to Prevent Unintended Modifications?
def modify_value_copy(lst):
    a=lst[:]
    a.append(5)
    print("Inside function:",a)
num=[1,2,3]
modify_value_copy(num)
print("Outside finction:",num)

# Lambda Functions
#regular expression
def square(num):
    return num*num
print(square(5))

#lambda expression
square_lambda = lambda num:num*num
print(square_lambda(5))

a=lambda x: x%2==0 if True else False
num=int(input("Enter a num:"))
print(a(num))

#normal function
def add(a,b):
    return a+b
print(add(3,5))        

#lambda function
add=lambda a,b:a+b
print(add(1,7))

#normal function
def max_number(a,b):
    if a>b:
        return a
    else:
        return b
print(max_number(10,20))

#lambda function
max_number=lambda a,b:a if a>b else b
print(max_number(10,20))

#Using map() – Apply Function to Each Element
list_numbers=[1,2,3,4,5]
square_numbers=list(map(lambda x:x*x,list_numbers))
print(square_numbers)

#Using filter() – Keep Only True Values
numbers=[1,2,3,4,5,6,7,8]
evens=list(filter(lambda x:x%2==0,numbers))
print(evens)

#Using reduce() – Reduce a List to a Single Value
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)

#Lambda Function with Lists & Sorting
#Sorting a List of Tuples
students=[("Aditya",85),("Balu",92),("Chai",78)]
sorted_students=sorted(students,key=lambda x:x[1])
print(sorted_students)

#Lambda Function in Dictionaries
gardes={"Aditya":85,"Balu":78,"Mani":99}
sorted_gardes=dict(sorted(gardes.items(),key=lambda item:item[1]))
print(sorted_gardes)

#Lambda with Default Arguments
greet=lambda name="Guest":f"Hello {name}!"
print(greet("Eswar"))
print(greet())

#Lambda Inside Another Function (Nested Lambda)
def multiple_by(a):
    return lambda x:x*a
double=multiple_by(2)
triple=multiple_by(3)
print(double(5))
print(triple(5))



