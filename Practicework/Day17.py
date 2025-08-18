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
'''
#pattern J
n=7
for i in range(n):
    for j in range(n):
        if i==0  or (i==n-1 and j<n//2) or j==n//2   :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
