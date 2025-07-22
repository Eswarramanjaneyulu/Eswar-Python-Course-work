#1. Check if a number is a 4-digit even number
print("4-digit number".center(20," "))
a=int(input("Enter a number: "))
if a>999 and a<=9999:
     print("It's a 4-digits number")
     if a%2==0:
          print("It's a 4-digits and even number")
     else:
          print("It's a 4-digits and odd number")
else:
     print("It's not a 4-digits number ")
  
#2. Check if a character is a consonant
a=input("Enter a letters: ").lower()
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    print("vowel")
else:
    print("Consonant")

#3. Check if a number is divisible by 2 or 3 but not both
a=int(input("Enter a number: "))
if a%2==0 and a%3==0:
    print("Divisible by both 2 and 3")
elif a%2==0:
    print("Divisible by 2 only") 
elif a%3==0:
    print("Divisible by 3 only")
else:
    print("Not Divisible by 2 and 3")

#4.Check if a number is negative and odd
a=int(input("Enter a number: "))
if a<0 and a%2==1:
    print("Negative and odd number")
elif a<0 and a%2==0:
    print("Negative and even number")
else:
    print("positive number") 

#5. Check if a string starts with a vowel
a=input("Enter a letters: ").lower()
if a[0]=='a' or a[0]=='e' or a[0]=='i' or a[0]=='o' or a[0]=='u':
    print("Start with a vowel")
else:
    print("Consonant")

#6. Check if three sides form a valid triangle
a=input("Enter a triangle numbers: ").split()
if len(a)==3:
    print("Valid triangle")
else:
    print("Not Valid triangle")

#7. Find the greatest among three numbers
a=input().split()
b=max(a)
print(b,"is the greatest")

#8. Check if a year is a century year and leap year
a=int(input("Enter a year: "))
if a%4==0 and (a%100!=0 or a%400==0):
    print("Century leap year")
else:
    print("Century not leap year")

#9. Check if a character is a digit
a=input("Enter a data: ")
if a.isdigit()==True:
    print("Digit")
else:
    print("char")
    
#10. Check if a number is palindrome (integer)
a=input("Enter a number:")
b=a[::-1]
if a==b:
    print("Palindrome number")
else:
    print("not Palindrome number")

#11. Compare lengths of two strings
a=input().split()
a1=input().split()
if a>a1:
    print("Second string is longer")
else:
    print("First string is longer")

#12. Check if a number is within a specific range (50 to 100) and divisible by 5
a=int(input("Enter a number: "))
if a>=50 and a<=100 and a%5==0:
    print("In range and divisible by 5")
elif  a>=50 and a<=100:
    print("In range but not divisible by 5")
elif a%5==0:
    print("Not range but divisible by 5")
else:
    print("Not range")
    
#13. Validate if a password length is strong (8 or more characters)
a=input("Enter a Password: ")
if len(a)>=8:
    print("Strong password")
else:
    print("Weak password")

#14. Check if sum of two numbers is even
a=int(input("Enter a num1: "))
b=int(input("Enter a num2: "))
c=a+b
if c%2==0 :
    print("Sum is even")
else:
    print("Sum is odd") 

#15. Check if the character is a special symbol (!, @, #, etc.)
a=input("Enter a character: ")
if a=='!' or a=='@' or a=='#' or a=='$':
    print("Special character")
else:
    print("it's a character")

#16. Check if temperature is cold (<15°C), moderate (15-30°C), or hot (>30°C)
a=int(input("Enter a temperature: "))
if a<15:
    print("Cold")
elif a>=15 and a<30:
    print("Moderate")
else:
    print("Hot")

#17. Check if a number lies outside the range 10 to 50
a=int(input("Enter a number: "))
if a>=10 and a<=50:
    print("In the range")
else:
    print("Outside the range")

#18. Check if number is a perfect square (basic method)
a=int(input("Enter a number1: "))
if (a**0.5)**2==a:
    print("Perfect square")
else:
    print("Not Perfect square")

#19. Compare two ages and determine who is older or if same age
a=int(input("Enter a age 1: "))
b=int(input("Enter a age 2: "))
if a<b:
    print("Second person is older")
else:
    print("First person is older")

#20. Check if an angle is acute, right, or obtuse
a=int(input("Enter an angle: "))
if a==90:
    print("Right angle")
elif a<90:
    print("Acute angle")
elif a<=180 and a>90:
    print("Obtuse angle")
else:
    print("Not angle")
