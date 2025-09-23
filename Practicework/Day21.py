#Recursive Functions
#Example 1: Factorial of a Number

def factorial_number(n):
    if n==0 or n==1:
        return 1
    else:
        a= n*factorial_number(n-1)
        return a
num=int(input())
print(factorial_number(num))

l=list(map(int,input().split(',')))
sum=0
for i in l:
    sum+=i
print(sum)

a=list(map(int,input().split(',')))
print(max(a))
print(min(a))

a=list(map(int,input().split(',')))
max=a[0]
min=a[0]
for i in a:
    if i>max:
        max =i
    if i<min:
        min =i       
print(max)
print(min)

a=list(map(int,input().split(',')))
l=[int(item) for item in a]

newl=[]
for i in l:
    if i in newl:
        continue
    else:
        newl.append(i)
print(newl)

a=list(map(int,input().split(',')))
b=set(a)
c=list(b)

print(c)

a=list(map(int,input().split(',')))
c=int(input())
b=a.count(c)
print(f"count of {c} = {b}")

a=list(map(int,input().split(',')))
c=int(input())
count=0
for i in a:
    if i==c:
        count+=1
print(f"count of {c} = {count}")

a=list(map(str,input().split(',')))
print(a[0])    
print(a[1])    
print(a[2])    
print(a[3])    
print(a[-1])    

a=set(map(int,input().split(',')))
b=set(map(int,input().split(',')))
c=a.union(b)
d=a.intersection(b)
print(c)
print(d)

a={"name":"Eswar","age":22,"city":"kakinada"}
my_dict={}
name=input("Enter a name: ")
age=int(input("Enter a age: "))
city=input("Enter a city: ")
my_dict["name"]=name
my_dict["age"]=age
my_dict["city"]=city
print(my_dict)

a=input().split(',')
print(a)
a[0]=input()
print(a)

a=list(map(int,input().split(',')))
a.sort()
print(a)

a=list(map(int,input().split(',')))
b=list(map(int,input().split(',')))
c=a+b
print(c)

s=[x**2 for x in range(1,6)]
print(s)
