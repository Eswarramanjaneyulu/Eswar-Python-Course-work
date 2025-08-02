#1. Check if three lengths form an Equilateral, Isosceles, or Scalene triangle
'''
a,b,c=tuple(map(int,input("Enter a numbers: ").split()))
if a==b and a==c and b==c:
    print("Equilateral triangle")
elif a!=b and a!=c and b!=c:
    print("Scalene triangle")
else:
    print("Isosceles triangle")

#2.Classify a character as: vowel, consonant, digit, special character
a=input("Enter a  data: ")
vol="aeiouAEIOU"
if a.isalpha():
    if a in vol:
        print("Vowel")
    else:
        print("Consonant")

elif a.isdigit():
    print("Digit")
else:
    print("Special character")

#3. BMI Calculator and Category
height=float(input("Enter a height: "))
weight=float(input("Enter a weight: "))
BMI = weight/(height*height)

if BMI >25:
    print("Overweight")
elif BMI <25:
    print("Underweight")
else:
    print("Perfect")

#4. Electricity bill calculator based on units used
a=int(input("Enter a bill: "))
bill=0
if a<=100:
    bill = a*1
elif a>100 and a<=200:
    bill = 100*1 + (a-100)*2
else:
    bill = 100*1 + 100*2 + (a-200)*3
    
print(bill) 

#5. Check if a number is Armstrong (3-digit)
a=input("Enter a numbers: ")
armstrong =0
for i in a:
    armstrong+=int(i)**len(a)
if int(a) == armstrong:
    print("Armstrong number")
else:
    print("Not Armstrong number")

#6. Validate strong password (min 8 chars, 1 uppercase, 1 digit, 1 special char)
a=input("Enter a password: ")
if len(a)>=8:
    s=set()
    for i in a:
        if i.isupper():
            s.add('U')
        elif i.islower():
            s.add('L')
        elif i.isdigit():
            s.add('D')
        else:
            s.add('S')
    if len(s)==4:
        print("Strong Password")
    else:
        print("Week Password")
else:
    print("Week Password") 

#7. ATM Withdrawal Simulation
balance,amount=tuple(map(int,input("Enter a amount: ").split()))

if amount<=balance:
    print("Success the balance left",balance-amount)
else:
    print("Not in your account")

#8. Ticket fare calculator with age-based discounts
a=int(input("Enter a Age: "))
price=int(input("Enter a ticket price: "))
if a<5:
    price="Free"
elif a>=5 and a<18:
    price=price-(price*0.5)
else:
    price=price-(price*0.3)
    
print(price)
'''
#9. 24-hour to 12-hour time converter

