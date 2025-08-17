a=list(map(int,input().split()))

for i in a:
    if i==1:
        print("You have unread notifications!")
        break
else:
    print("All Caught up!")

for i in range(5):                #i is outer loop it's rows
    for j in range(1,5):          #j is inner loop it's columns
        print(j,end=" ")
    print()
    
#square pattern
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()

for i in range(5):
    for j in range(5):
        print(i,end=" ")
    print()

for i in range(5):
    for j in range(5):
        print(j,end=" ")
    print()
    
#right angled triangle
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
#inverted rught angled triangle
for i in range(5):
    for j in range(i-1,4):
        print("*",end=" ")
    print()
    
#inverted rught angled triangle
for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print()
    
#revers right angled triangle
for i in range(5):
    for j in range(5-i-1):
        print(" ",end=" ")
    for col in range(i+1):
        print("*",end=" ")
    print()

#revers inverted rught angled triangle
for i in range(5):
    for j in range(i):
        print(" ",end=" ")
    for col in range(5-i):
        print("*",end=" ")
    print()

# space square pattern
n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==n//2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    

#pattern Z
n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==i/1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

# pattern X
n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if  i==j or j+i==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

 