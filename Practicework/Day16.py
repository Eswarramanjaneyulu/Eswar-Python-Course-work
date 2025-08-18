'''
#pattern A
n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==0 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#pattern E
r=int(input("Enter a size: "))
c=int(input("Enter a size: "))
for i in range(r):
    for j in range(c):
        if j==0 or j==r-1 or i==0 or i==r-1 or i==r//2  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#pattern B
r=int(input("Enter a size: "))
for i in range(r):
    for j in range(r):
        if j==0 or (j==r-1 and i!=0 and i!=r//2 and i!=r-1) or (i==0 and j!=r-1) or (i==r-1 and j!=r-1) or (i==r//2 and j!=r-1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()   

#pattern C
n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if (i==0 and j!=0) or (i==n-1 and j!=0) or (j==0 and i!=0 and i!=n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#pattern D
n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if (i==0 and j!=n-1 ) or (i==n-1 and j!=0 and j!=n-1) or j==0  or (j==n-1 and i!=0 and i!=n-1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#pattern E
n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if j==0 or (j==n-1 and j!=n-1) or i==0 or i==n-1 or i==n//2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#pattern F
n=5
for i in range(n):
    for j in range(n):
        if j==0 or (j==n-1 and j!=n-1) or (i==0 and j!=n-1)  or (i==n//2 and j!=n-1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#pattern G
n=5
for i in range(n):
    for j in range(n):
        if (i==0 and j!=0) or (i==n-1 and j!=n-1 ) or (j==0 and i!=0) or (j==n-1 and i!=n-4) or (j==n-2 and i!=n-4 and i!=n-2) or (j==n-3 and i!=n-4 and i!=n-2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
   
#pattern H
n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
