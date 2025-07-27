'''
# 1. Square Pattern
a=int(input())
for i in range(a):
    for j in range(a):
        print("*",end=" ")
    print()   


# 2. Right-Angled Triangle
a=int(input())
for i in range(a):
    for j in range(i+1):
        print("*",end=" ")
  print()

# 3. Inverted Right-Angled Triangle
a=int(input())
for i in range(a,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

# 4. Pyramid Pattern
a=int(input())
for i in range(a):
    print(' ' * (a-i-1)+'* ' *(i+1))
'''
a=int(input())
for i in range(1,a+1):
    for j in range(i):
        print("*",end=" ")
    print()



'''
a=int(input("Enter anumber: "))
for i in range(a):
    print("*",end=" ")
for j in range(a):
    if j%2==0:
        print("*",end=" ")
for i in range(a):
    print("*")
'''