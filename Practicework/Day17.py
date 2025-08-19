'''
#pattern I
n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n//2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#pattern J
n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if i==0  or (i==n-1 and j<n//2) or j==n//2   :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#pattern K
n=7
for i in range(n):
    for j in range(n):
        if j==0  or (i==n//2 and j<=1) or (i==1 and j==n<=3) or (i==0 and j>2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#pattern L
n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#pattern M
n=int(input("Emter a Size: "))
for i in range(n):
    for j in range(n):
        if j==0 or (i==j and j<=n//2) or (j+i==n-1 and j>=n//2) or j==n-1   :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#pattern N
n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1  or i==j  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#pattern O
n=int(input("Enter a size: "))
for i in range(n):
    for j in range(n):
        if (i==0 and j!=0 and j!=n-1) or (j==0 and i!=0 and i!=n-1) or (i==n-1 and j!=n-1 and j!=0) or (j==n-1 and i!=n-1 and i!=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#pattern P
n=5
for i in range(n):
    for j in range(n):
        if (i==0 and j!=0 and j!=n-1) or (j==0 and i!=0) or (i==n//2 and j!=n-1) or (i==1 and j>=4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()