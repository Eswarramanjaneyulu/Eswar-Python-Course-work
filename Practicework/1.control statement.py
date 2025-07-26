'''
#1. Print Numbers from 1 to N (Using for loop)
n=int(input("Enter a number: "))
for i in range(n):
    print(i)
    
#2. Print Even Numbers from 1 to N (Using for loop)
n=int(input("Enter a number: "))
for i in range(0,n,2):
    print(i)

#3. Sum of Numbers from 1 to N (Using for loop)
a = int(input("Enter a number: "))
total = 0
for i in range(1,a+1):
    total+=i
print(total)

#4. Print Odd Numbers from 1 to N (Using for loop)
n=int(input("Enter a number: "))
for i in range(n):
    if i%2!=0:
        print(i)

#5. Find Factorial of a Number (Using for loop)
a=int(input("Enter a number: "))
factorial=1
for i in range(1,a+1):
    factorial*=i
print(factorial)

#6. Print Multiplication Table of N (Using for loop)
a=int(input("Enter a number: "))
for i in range(1,11):
    print(a*i)   

#Check Prime Number (Using for loop)
a=int(input("Enter a number: "))
if a<=1:
    print("Not Prime")
else:
    for i in range(2,a):
        if a%i==0:
            print("Not Prime")
    else:
        print("Prime")           
'''          
#Sum of Digits of a Number (Using while loop)
a=int(input("Enter a Number: "))