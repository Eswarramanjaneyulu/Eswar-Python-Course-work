#1.positive or negative
a=int(input("Enter a number : "))
if a>0:
    print("positive number")
else:
    print("negative number")
 
 #even or odd
a=int(input("Enter a number :  "))   
if a % 2 ==0:
     print("even")
else:
     print("odd")
     
#Divisible by 5
a=int(input("Enter a number : "))
if a%5==0:
     print("Divisible by 5")
else:
     print("not divisable by 5")
     
#divisable by 3and 7
a=int(input("Enter a number : "))
if a%3==0 and a%7==0:
     print("Divisible by both 3 and 7")
elif a%3==0 :
     print("Divisible by  3 ")
elif a%7==0 :
     print("Divisible by 7")
else:
     print("none")
     
#check for leap year
a=int(input("Enter a year : "))
if a%4==0 and a%100!=0:
     print("it is a leap year")
else:
     print("its is a not leap year")
     
#Check Pass or Fail (Passing marks = 35)
a=int(input("Enter a marks:"))
if a>=35:
     print("pass")
else:
     print("fail")  
     
#check if number is 3-digit
digit=int(input("Enter a number:"))
if 100<= digit <=999:
     print("it's a 3-digit number")
else:
     print("it's not a 3-digit number")
     
digit = int(input("Enter a number"))
if digit>=100 and digit <=999:
     print("it's a 3-digit number")
else:
     print("it's not a 3-digit number")
     
#check if character is vowel
char=input("Enter a character: ").lower()
if char=='a' or char=='e' or char =='i' or char =='o' or char =='u' :
     print("its a vowel") 
else:
     print("it's not vowel")
#Check greatest of two numbers
     
    
a=int(input("Enter a num1:"))
b=int(input("Enter anum2:"))
if a<b:
     print(b,"is greater")
elif b<a:
     print(a,"is grater")
else:
     print("equal number")
     
#Check smallest of two numbers
     
a=int(input("Enter a num1:"))
b=int(input("Enter anum2:"))
if a>b:
     print(b,"is smaller")
elif b>a:
     print(a,"is smaller")
else:
     print("equal number") 
     
#check if number is zero
a=int(input("Enter a number: "))
if a==0:
     print("Number is zero")
else:
     print("it is a number" )
     
#check if number is multiple of 10
a=int(input("Enter a number: "))
if a%10==0:
     print("Multiple of 10")
else:
     print("Not Multiple 10 ")
     
#Check if age is eligible to vote (18+)
a=int(input("Enter your age: "))
if a>=18:
     print("Eligible to vote")
else:
     print("Not Eligible to vote")
     
#Check if number is between 1 and 100
a= int(input("Enter a number: "))
if a>1 and a<100:
     print("In Range")
else:
     print("Not Range")
     
#15. Check if number is square of another
a=int(input("Enter a number1: "))
b=int(input("Enter a number2: "))
if a == b **2:
     print(a,"is square of ",b)
else:
     print(a,"is not square of ",b)

#16. Check if two strings are equal
a=input("Enter a name1: ")
b=input("Enter a name2: ")
if a==b:
     print("strings are equal")
else:
     print("not equal")
     
#17.Check if a number is prime (basic logic)
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

#18. Check if number is positive and even
a=int(input("Enter a number: "))
if a%2==0 and a>1:
     print("Positive and even number") 
else:
     print("Not Positive and even number")

#19. Check if character is uppercase
a=input("Enter a Character: ")
if a.isupper():
     print("Uppercase letter")
else:
     print("not an uppercase letter")

#20. Check if temperature is hot (>30°C)
a=int(input("Enter a temperature: "))
if a>30:
     print("it's hot")
else:
     print("it's cool")