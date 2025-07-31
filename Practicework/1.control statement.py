#1. Print Numbers from 1 to N (Using for loop)
'''
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
        #(or)    
a=int(input("Enter a Number: "))
for i in range(1,a,2):
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
      #(or)
a=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{a}*{i}={a*i}")  
    
#7 Check Prime Number (Using for loop)
a=int(input("Enter a number: "))
if a<=1:
    print("Not Prime")
else:
    for i in range(2,a):
        if a%i==0:
            print("Not Prime")
    else:
        print("Prime")           
        
#8 Sum of Digits of a Number (Using while loop)
a=int(input("Enter a number: "))
b=1
sum=0
while b<=a:
    sum =b+sum
    b+=1
print(sum)
   
#9. Print Fibonacci Sequence up to N Terms (Using for loop)
n=int(input("Enter a number: "))
a,b=0,1
print("Fibonacci sequence: ")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

#10. Count Numbers Divisible by 3 (Using for loop)
a=int(input("Enter a number: "))
count=0
for i in range(1,a+1):
    if i%3==0 :
        count+=1
print("Count of numbers divisible by 3 from 1 to", a, "is:", count)

#11. Check if a Number is Palindrome (Using while loop)
num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")
'''