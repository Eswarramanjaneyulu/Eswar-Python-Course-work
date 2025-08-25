#Function Arguments
#1. Positional Arguments
def positional_argument(name,age):
    print(f"Hello {name} are you {age} years old!")
name=input("Enter a Name: ")
age=int(input("Enter a Age: "))
positional_argument(name,age)

#2. Keyword Arguments
def keyword_argument(name,age):
    print(f"Hello {name} are you {age} years old!")
name=input("Enter a Name: ")
age=int(input("Enter a Age: "))
keyword_argument(age=age,name=name)

#3. Default Arguments
def default_argument(name,age=22):
    print(f"Hello {name} are you {age} yeras old!")
name=input("Enter a name: ")
default_argument(name)    

#4. Variable-Length Arguments
#*args (Arbitrary Positional Arguments)
def add(*num):
    return sum(num)
num=eval(input())
print(add(*num))

#1. Positional Arguments
def add(a,b):
    return a+b
num1=int(input())
num2=int(input())
print(add(num1,num2))

#2.keywords arguments
def add(a,b):
    return a+b
num1=int(input())
num2=int(input())
print(add(b=num1,a=num2))

#3.defalut argument
def add_strings(greatings,name="Eswar"):
    return greatings + ","+ name +"!"
greating1=add_strings("Hello")
greating2=add_strings("Hi","Ram")
print(greating1)
print(greating2)

#4.Scpe of variables
# EX:-
def add(a,b):
    sum=a+b
    print(sum)
add(7,18)

#4.1.global scope
global_var=10
def fun():
    print(global_var)
fun()
print(global_var)

#4.2.local variable
def fun():
    local_var=10
    print(local_var)
fun()

#lambda function
add=lambda x,y:x+y
print(add(7,18))

a=lambda x:x**2
print(a(5))


