#functions pre defined and user defined
# syntax
#def functino_name(parameters):
    # function body 

#add two numbers
def sum(a,b):
    print(a+b)
s1=int(input("Enter a number1:"))
s2=int(input("Enter a number2:"))
sum(s1,s2)

def add (a,b):
    return a+b
s1=int(input("Enter a number1:"))
s2=int(input("Enter a number2:"))
result=add(s1,s2)
print(result)
#add two strings
def add (a,b):
    return a+b
s1=input("Enter a number1:")
s2=input("Enter a number2:")
result=add(s1,s2)
print(result)

#length of string
def add (a):
    return a
s1=input("Enter a number1:")
result=add(s1)
print(len(result))

#key arguments
def info(name,age):
    print("Name:",name)
    print("Age:",age)
    
info(age=21,name="Eswar")

def info(name,age):
    print("Name:",name,"Age:",age)
    
info(age=21,name="Eswar")

def info(name,age):
    print("Name:",name)
    print("Age:",age)
name=input("Enter your name: ")
age=int(input("Enter your age: "))
    
info(name,age)

