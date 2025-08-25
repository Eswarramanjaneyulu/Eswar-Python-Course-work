#functions arguments
#1. Positional Arguments
def my_name_and_age(name,age):
    print(f"Hello! {name} are you {age} years old!")
Name=input("Enter a Name: ")
Age=int(input("Enter a Age: "))
my_name_and_age(Name,Age)

def my_name_and_age(name,age):
    return f"Hello! {name} are you {age} years old!"
Name=input("Enter a Name: ")
Age=int(input("Enter a Age: "))
print(my_name_and_age(Name,Age))

#2.keyword argument
def my_name_and_age(name,age):
    print(f"Hello! {name} are you {age} years old!")
Name=input("Enter a Name: ")
Age=int(input("Enter a Age: "))
my_name_and_age(age=Age,name=Name)

def my_name_and_age(name,age):
    return f"Hello! {name} are you {age} years old!"
Name=input("Enter a Name: ")
Age=int(input("Enter a Age: "))
print(my_name_and_age(age=Age,name=Name))

#3.default argament
def my_name_and_age(name,age=22):
    print(f"Hello {name} are you {age} years old!")
Name=input("Enter a name: ")
my_name_and_age(Name)    

def my_name_and_age(name,age=22):
    a= f"Hello {name} are you {age} years old!"
    return a
Name=input("Enter a name: ")
print(my_name_and_age(Name))

#4. Variable-Length Arguments
#4.1.*args (Arbitrary Positional Arguments)
def add(*a):
    add=sum(a)
    return add
print(add(1,2))

#4.2.*args (Arbitrary Positional Arguments)
def user_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

user_info(name="Alice", age=25, city="New York")

#5.Scope of Variables
#1.local scope
def my_name():
    name="Eswar"
    return name
print(my_name())

#2.global scope
name="Eswar"
def my_name():
    return name
print(my_name())

a=10
def num():
    return a
print(num())
a=7
print(num())

