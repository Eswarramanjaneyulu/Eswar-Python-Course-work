#syntax of parameters (definations)
#def-(key word) function_name(parameters):
    #function body
#syntax of argument(calls) (it will use call a function)
#function_name(argument)
#functions
def function(a):
    return f"Hello,{a}"
a=input()
print(function(a))

#1.types of functions
def type_functions(a):
    return a
a=input("Enter a name: ")
print(type_functions(len(a)))
print(type_functions(max(a)))
print(type_functions(sorted(a)))
print(type_functions(abs(-10)))

#2. User-Defined Functions
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def floor_div(a,b):
    return a//b
def exponations(a,b):
    return a**b
def module(a,b):
    return a%b
a=int(input("Enter a num1: "))
b=int(input("Enter a num2: "))
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
print(floor_div(a,b))
print(exponations(a,b))
print(module(a,b))

def function(a):
    return f"Hello,{a}"
name=input()
print(function(name))

def add(a,b):
    print(a+b)
num1=int(input())
num2=int(input())
add(num1,num2)

def len_string(a):
    return len(a)
str1=input()
print(len_string(str1))



