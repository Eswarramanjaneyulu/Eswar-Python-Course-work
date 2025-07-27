# loops
'''
while condition
#
#
#
process
'''
'''
#while loop
candies=10
while candies>0:
    print("Giving a candy to a friend:")
    candies-=1
print(candies)

#for loop
#for variable in range(start,stop,step):
candies = 10
for i in range(candies):
    print("give candies to a friends")

a="hello world"
for i in a:
    print(i)
 
a="hello world"  
for i in range(len(a)):
    print(i)

#nested loop
for i in range(1,6):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")

#break
candies = 10

for i in range(candies):
    print("giving a candies to a friend")
    
    if candies -i ==5:
        print("only 5 candies left. stooping distribution ")
        break

#continue
candies = 10

for i in range(candies):
    
    if candies- i == 5:
        print("only 5 candie left. skipping this turn")
        continue
    
    print("giving a candies to a friend",i)

#for loop
a=int(input("Enter a number: "))
for i in range(1,6):
    print(i)

#while loop
a=int(input("Enter a number: "))
i=1 
while i<=a:
    print(i) 
    i+=1

a=int(input("Enter a number: "))
for i in range(a):
    print(a-i)
    
a=int(input("Enter a number: "))
i=1 
while i<=a:
    print(i) 
    a-=i
    break

a=int(input("Enter a number: "))
b=1
sum=0
while b<=a:
    sum += b
    b+=1
print(sum)

a=int(input("Enter a number: "))    
i=1
while i<=a:
    if i%2==0:
        print(i)
    i+=1

a=int(input("Enter a number: "))    
i=1
while i<=a:
    if i%2!=0:
        print(i)
    i+=1   

a=int(input("Enter a number: "))    
i=1
while i<=10:
    print(f"{a}X{i}={a*i}")
    i+=1

a=int(input("Enter a number: "))  
f=1 
while a>0:
    f=f*a
    a-=1
print(f)

a=int(input("Enter a number: "))  
f=1
for i in range(a):
    f=f*a
    a-=1
print(f)
'''
