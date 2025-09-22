'''
names=input("Enetr a names: ").split()
print(names)

names=input("Enetr a names: ").split(",")
print(names)

marks=list(map(int,input("Enter a marks: ").split()))
print(marks)

a=list(map(float,input("Enter a weights: ").split()))
print(a)

a=tuple(map(int,input("Enter a data: ").split()))
print(a)

a=set(map(int,input("Enter a data: ").split()))
print(a)

a=eval(input("Enter a data: "))
print(a)

a,b=input("Enter a and b : ").split()
print(a)
print(b)

a=input("Enetr a name: ")
print(a)
print(a[0])
print(len(a))
print(max(a))
print(min(a))

a="eswar","hello","eswar","ram"
print(a.count("hello"))

a=int(input())
is_prime=True
if a<=1:
    is_prime = False
else:
    for i in range(2,a):
        if a%i==0:
            is_prime =False
            break
if is_prime:
    print("Prime number")
else:
    print("Not prime")

def greet(name):
    print(f"Hello {name}")
    print(f"Good maorining")
a="Eswar"
greet(a)

def greet(a,b):
    print(f"Hello {a}!")
    print(f"Hello {b}, nice to meet you!")
x="Eswar"
y="Sir"
greet(x,y)

def greet(name="user"):
    print(f"Hello",name)
user_name=input()
greet(user_name)
greet()

def add(a,b):
    sum=a+b
    print(sum)
add(7,7)

def getsum(*x):
    result =0
    for a in x:
        result +=a
    print(result)
getsum(10,20,30,40)

def fun(name,age,country="INDIA"):
    print("Name:",name)
    print("Age:",age)
    print("I am from",country)
fun(age=23,name="Eswar")

def add(*nums):
    result=0
    for i in nums:
        result+=i
    return result
a=add(10,20,30,40)
print(a)

def greet(name,age):
    print(f"Hello {name}, you are {age} years old!.")
greet("Eswar",23)
greet(23,"Eswar")# X worng
greet(age=23,name="Eswar")

def greet(name,age=23):
    return f"Hello {name}, you are {age} years old!."
print(greet("Eswar"))

def add(*num):
    return sum(num)
a=tuple(map(int,input().split(',')))
print(add(*a))
    #(OR)
def add(*num):
    return sum(num)
print(add(1,2,3,4,5))

def user_info(**detials):
    for keys,values in detials.items():
        print(f"{keys}:{values}")
user_info(name="Eswar",age=23,city="Kajuluru")

x=10
def greet():
    global x
    x=20
greet()
print(x)

def outer():
    m="Hi"
    def inner():
        print(m)
    inner()
outer()

def outer():
    m="Hi"
    def inner():
        nonlocal m
        m="Hello"
    inner()
    print(m)
outer()

def person(*data):
    print(data)
person("Eswar",23,9014584004,"Kajuluru")

def person(**data):
    print(data)
person(Name="Eswar",age=23,mobile=9014584004,city="Kajuliru")

def person(**data):
    for key,value in data.items():
        print(f"{key} : {value}")
person(Name="Eswar",age=23,mobile=9014584004,city="Kajuliru")

def person(**data):
    for key,value in data.items():
        print(f"{key} : {value}")
name=input("Enter a name: ")
age=int(input("Enter a age: "))
mobile=input("Enter a mobile: ")
city=input("Enter a city: ")
person(Name=name,Age=age,Mobile=mobile,City=city)

def person(**data):
    for key,value in data.items():
        print(f"{key} : {value}")
a=1
while a!='0':
    name=input("Enter a name: ")
    age=int(input("Enter a age: "))
    mobile=input("Enter a mobile: ")
    city=input("Enter a city: ")
    print('')
    person(Name=name,Age=age,Mobile=mobile,City=city)
    a=input("Enter a zero to exit or any key to countinue: ")
'''