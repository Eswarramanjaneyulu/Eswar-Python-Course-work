a= input("enter your data: ").split('-')
a=a[::-1]
print('/'.join(a))

date,mounth,year=input("Enter a DOB: ").split()
print(f"{year}/{mounth}/{date}")

num=int(input(("Enter a number: ")))
if num%2==0:
    print("Even Winner")
else:
    print("Odd Winner")

data = input("Enter a string: ")
data=data.replace('a','*')
data=data.replace('e','*')
data=data.replace('i','*')
data=data.replace('o','*')
data=data.replace('u','*')
print(data)

a=list(map(float,input("Enter a price: ").split()))
print(sum(a))
print(max(a))

a,b=("admin","python123")
username=input("Enter a username: ")
password=input("Enter a password: ")
if username==a and password==b:
    print("Login Successful")
else:
    print("Access Denied")

a=set(map(str,input("Enter a name: ").split()))
print(a)

data = int(input("Enter number of students: "))

student ={}

for _ in range(data):
    entry=input().split()
    name=entry[0]
    marks=int(entry[1])
    student[name]=marks
    
topper = max(student,key=student.get)

print("First Ranker:",topper)

a=input("Enter a string: ")
b=[word[::-1] for word in a.split()]
c=' '.join(b)
print(c)

a=list(map(int,input("Enter a list: ").split()))
b=[]
for item in a:
    num=int(item)
    if num !=0:
        b.append(num)
print(b)

a=input()
b={}
for char in a:
    if char !=' ':
        if char in b:
            b[char]+= 1
        else:
            b[char]=1
print(b)           
            
        