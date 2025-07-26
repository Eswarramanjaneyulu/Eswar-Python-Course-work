print("code is ended") 
#string
a="eswar"
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])

# string slicing
a="Hello World!"
print(a[1])
print(a[-1])
print(a[1:3])
print(a[1:-1])
print(a[:3])
print(a[2:])
print(a[:-1])
print(a[::2])
print(a[1::2])
print(a[::-1])

a="Hello World"
print(a[1:2])
print(a[-1:])
print(a[1:3])
print(a[1:10])
print(a[:3])
print(a[2:])
print(a[:10])
print(a[::2])
print(a[1::2])
print(a[::-1])

a="hello"
b="world"
print(a +" "+ b)

a=" eswar ram "
print(len(a))
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace('e','E'))
print(a.count('r'))
print(a.capitalize())
print(a.title())
print(a.lstrip())
print(a.rstrip())
print(a.startswith(" "))
print(a.endswith(" "))
print(a.join("a"))
print(a.find("a"))
print(a.rfind("a"))
print(a.index("r"))
print(a.rindex("r"))
print(a.isalnum())
print(a.isalpha())

a=" hello world "
b=a.center(50, "*")
print(b)

#string formatting
name="eswar"
age=21
print(f"my name is %s and i am %d years old" % (name,age))
print("my name is {} and i am {} years old".format(name,age))
print(f"my name is {name} and i am {age} years old")

#Escape sequences
print("eswar\' ram") #single quote
print("eswar\n' ram") #new line 
print("eswar\t ram") #tab
print("eswar\r ram") #carriage return
print("eswar\b ram") #backspace
print("eswar\f ram") #form feed
print("eswar\v ram") #veritacal feed
print("eswar\\ ram") #backslash

s=input("Enter a data: ").lower()
a=s.count("a")
e=s.count("e")
i=s.count("i")
o=s.count("o")
u=s.count("u")

print(f"Number of vowels:{a+e+i+o+u}")

#grade calculator
a=int(input("Enter a marks in maths: "))
b=int(input("Enter a marks in science: "))
c=int(input("Enter a marks in english: "))

total_marks=a+b+c
averge =total_marks/3

percentage = (total_marks/300)*100
garde =  ""
if percentage > 90:
    garde = "A+"
elif percentage <=90 and percentage>80:
    garde ="A"
elif percentage <=80 and percentage>70:
    garde="B"
elif percentage<70 and percentage>60:
    garde = "C"
elif percentage<=60 and percentage>50:
    garde ="D"
elif percentage<=50 and percentage>34:
    garde="E"
else:
    garde="F"
print(f"Total marks:{total_marks}\n Average marks:{averge}\n Percentage:{percentage}\n Garde:{garde}")
#pallindrome or not
a=input("Enter a data: ")
b=a[::-1]
if b==a:
    print("It's a pallindrome")
else:
    print("Not pallindrome")
# largest number in many numbers
a=list(map(int,input().split()))
b=max(a)
print(b)

#leap year
a=int(input("Enter a year: "))
if (a%100==0 or a%4==0) and a%400!=0:
    print("leap year" )
else:
    print("not")

#Temperature convert
a=int(input("Enter a temperature: "))
b=input("Enter a units: ")
c="kelvin"  
d="fahrenheit"  
e="celises"
if b==c:
    print(f"Temperature in {c}: {a}{b[:1]}")
elif b==d:
    print(f"Temperature in {d}: {a}{b[:1]}")
elif b==e:
    print(f"Temperature in {e}: {a}{b[:1]}")
else:
    print("nothig")