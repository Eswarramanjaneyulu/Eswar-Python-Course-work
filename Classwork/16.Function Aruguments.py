#Function Arguments
#1. Positional Arguments

def greet(name,age):
    print(f"Hello {name}, you are {age} years old.")
a=input("Enter a Name: ")
b=int(input("Enter a Age: "))
greet(a,b)

#2. Keyword Arguments
def greet(name,age):
    print(f"Hello {name}, you are {age} years old ")
a=input("Enter a Name: ")
b=int(input("Enter a Age: "))
greet(name=a,age=b)

#3. Default Arguments
def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")
a=input()
greet(a)

#4. Variable-Length Arguments
#*args (Arbitrary Positional Arguments)
def add(*numbers):
    return sum(numbers)
numbers=list(map(int,input().split(",")))
print(add(*numbers))

#**kwargs (Arbitrary Keyword Arguments)
def user_info(**details):
    for key,value in details.items():
        print(f"{key}: {value}")

a=input("Enter a Name: ")
b=int(input("Enter a Age: "))
c=input("Enter a City: ")
user_info(name=a, age=b, city=c)

#Scope of Variables
#1. Local Scope
def greet():
    message = input()
    print(message)
greet()

#2. Global Scope
x = int(input())
def show():
    print(x)
show()
# or
x=10
def update():
    global x
    x=20
update()
print(x)

#3. Enclosing Scope (Nonlocal Scope)
def outer():
    msg="Hi"
    def inner():
        msg1="Eswar"
        print(msg)
        print(msg1)
    inner()
outer()

#4. Built-in Scope
def len_str(a):
    return len(a)
a=input()
print(len_str(a))

#LEGB Rule Summary
a="global"
def outer():
    a="enclosing"
    
    def inner():
        a="local"
        print(a)
    inner()
outer()

#Shadowing Variables
a=100
def fun():
    a=50
    print(a)
    
fun()
print(a)




