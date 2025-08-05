#1. What is a List?
'''
numbers=list(input("Enter a numbers: "))
names=list(input("Enter a names: "))
mixed=list(input("Enter a mixed: "))
print(type(numbers))
print(type(names))
print(type(mixed))
print(numbers)
print(names)
print(mixed)

#2.List Comprehension?
# syntx of [expression for item in iterable if condition]
#a. Square numbers in a range:
a=int(input())
squares=[x*x for x in range(a)]
print(squares)

def squares(a):
    return [x*x for x in range(a)]
a=int(input())
print(squares(a))

#b. Filter even numbers:
numbers = list(map(int,input().split()))
evens = [n for n in numbers if n % 2 == 0]
print(evens)

def even_numbers(numbers):
    return [a for a in numbers if a%2==0]
numbers=list(map(int,input().split()))
print(even_numbers(numbers))

#c. Uppercase a list of strings:
names=eval(input())
upper_names=[name.upper() for name in names]
print(upper_names)

def upper_case(names):
    return [name.upper() for name in names]
names=eval(input())
print(upper_case(names))
'''
#5. Create Lists and Apply List Comprehensions




