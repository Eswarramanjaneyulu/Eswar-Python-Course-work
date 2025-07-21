#Conditional Statements
#1. if Statement
a=int(input("Enter a integer: "))
if a>0:
    print("It's a positive Integer")
    
#2. if-else Statement
a=int(input("Enter a integer: "))
if a>0:
    print("It's a positive Integer")
else:
    print("It's a negitive Integer")

#3. if-elif-else Statement
a=int(input("Enter a integer: "))
if a<=9 and a>0:
    print("It's a positive Integer but single digit")
elif a>9 : 
    print("It's a positive Integer but double digit")
else:
    print("It's a negitive Integer")

 #4. Nested Conditional Statements
num =int(input("Enter a number: "))
if num>0:
    print("it's positive number")
    if num%2==0:
        print("it's a even number")
    else:
        print("it's a odd number")
else:
    print("it's a negitive number")

#Practice Programming

print("Positive or Negative".center(5," "))
a=int(input("Enter a number: "))
if a>0:
    print("Positive number")

print("Even or Odd".center(10," "))
a=int(input("Enter a number: "))
if a%2==0:
    print("Even number")
else:
    print("Odd number")

print("Divisible by 3 and 7".center(7," "))
a=int(input("Enter a number: "))
if a%3==0 and a%7==0:
    print("Divisible by both 3 and 7")
elif a%3==0 and a%7!=0:
    print("Divisible by 3 ")   
elif a%3!=0 and a%7==0:
    print("Divisible by 7")
else:
    print("Not divisible by both 3 and 7")

print("Check for leap year")
a=int(input("Enter a year: "))
if a%4==0 and a%100!=0:
    print("Leap year")
else:
    print("not a leap year") 

print("Check Pass or Fail (Passing marks = 35)")
a=int(input("Enter a marks: "))
if a>=35:
    print("Pass")
else:
    print("Fail")

print("Check if number is 3-digit")
a=int(input("Enter a number: "))
if a>99 and a<=999:
    print("it's a 3 digit number")
else:
    print("not a 3 digit number")

print("Check if character is vowel")
a=input("Enter a letters: ").lower()
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    print("vowel")
else:
    print("Not")

print("Check greatest of two numbers")
a=int(input("Enter a numbers: "))
b=int(input("Enter a numbers: "))
if a>b:
    print(a,"is greater")
elif b>a:
    print(b,"is greater")
else:
    print("both are equal")

print("Check Smallest of two numbers")
a=int(input("Enter a numbers: "))
b=int(input("Enter a numbers: "))
if a<b:
    print(a,"is smaller")
elif b<a:
    print(b,"is smaller")
else:
    print("both are equal")

print("Check if number is zero")
a=int(input("Enter a number: "))
if a==0:
    print("Number is zero")
elif a<0:
    print("its negitive number")
else:
    print("its positive number")

print("Check if number is multiple of 10")
a=int(input("Enter a number: "))
if a%10==0:
    print("Multiple of 10")
else:
    print("Not Multiple of 10")

print("Check if age is eligible to vote (18+)")
a=int(input("Enter a age: "))
if a>18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

print("Check if number is between 1 and 100")
a=int(input("Enter a number: "))
if a>0 and a<=100:
    print("In range")
else:
    print("Not In range")

print("Check if number is square of another")
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
if a%b==0:
    print(a,"is square of",b)
else:
    print("Not square")
    
print("Check if two strings are equal")
a=input("Enter a word: ")
b=input("Enter a word: ")
if a==b:
    print("Strings are equal")
else:
    print("Strings are not equal")

print("Check if a number is prime (basic logic)")
num = int(input("Enter a number: "))
if num > 1:
    if num == 2 or num == 3:
        print("Prime number")
    elif num % 2 == 0 or num % 3 == 0:
        print("Not a prime number")
    elif num % 5 == 0 and num != 5:
        print("Not a prime number")
    else:
        print("Prime number")
else:
    print("Not a prime number")

print("Check if number is positive and even")
a=int(input("Enter a number: "))
if a>0 and a%2==0:
    print("Positive and even number")
elif a>0:
    print("Positive number")
else:
    print("Negitive number")

print("Check if character is uppercase")
a=input("Enter a letter: ")
if a==a.upper():
    print("Uppercase letter ")
else:
    print("Lowercase letter")

print("Check if temperature is hot (>30°C)")
a=int(input("Enter a temperature: "))
if a>=30:
    print("It's hot")
else:
    print("It's cool")