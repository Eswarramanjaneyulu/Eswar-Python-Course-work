#recursive function:
'''
n=input("Enter the number: ")
sum=0
for i in n:
    sum +=int(i)
    print(sum)   
    
n=int(input("Enter a value: "))
def sumofdigits(n):
    if n==0:
        return 0
    return n%10+sumofdigits(n//10)
print(sumofdigits(n))

n=int(input("Enter a number: "))
a=0 
b=1 
if n==1:
    print(a)
elif n>=2:
    print(b)

    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c

#Pattern Problems Using Nested Loops
print("Square Pattern")
a=5
for i in range(a):
    for j in range(a):
        print("*",end=" ")
    print()

print("Right-Angled Triangle")
a=5
for i in range(a):
    for j in range(i+1):
        print("*",end=" ")
    print()
   
print("Inverted Right-Angled Triangle") 
a=5
for i in range(a,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print("Pyramid Pattern")
n = 5 
for i in range(n):
    print(' ' * (n -i -1) + '* ' *(i + 1))
        
print("Diamond Pattern")     
n = 5
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))  

for i in  range (n-2,-1,-1):
    print(' ' * (n-i-1)+'* '*(i+1))

print("Number Triangle")
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print() 

for i in range(0,10):
    print(i)   
    
for i in range(0,10,2):
    print(i)  

a=[1,2,3,4,5]
for i in a:
    print(i)  

a="eswar"
for i in a:
    print(i)

k=10
while k<20:
    print("eswar")
    k+=1
'''