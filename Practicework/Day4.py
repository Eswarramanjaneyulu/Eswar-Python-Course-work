print("Hello")

#Input Formatting
#1.String Input
name = input("Enter your name: ")
print(name)

#2. Integer Input
number=int(input("Enter a number: "))
print(number)

#3.Float input
decimal=float(input("Enter a price: "))
print(decimal)

#4. Input as List (Space-separated)
list=input("Enter a names: ").split()
print(list)

#5.Input as List (Comma-separated)
list=input("Enter a names: ").split(',')
print(list)

#6. List of Integers
marks=list(map(int,input("Enter a marks: ").split()))
print(marks)

#7. List of Floats
a=list(map(float,input("Enter a price: ").split()))
print(a)

#8. Tuple Input
a=tuple(map(int,input("Enter a values: ").split()))
print(a)

#9. Set Input
a=set(map(int,input("Enter a Ids : ").split()))
print(a)

#10. Dictionary Input using eval()
a=eval(input("enater a dict: "))
print(a)

#11. Multiple Inputs with Unpacking
a,b=input("Enter a username and password: ").split()
print("Username:",a)
print("Password:",b)

#Output Formatting
#a) Printing Text
print("Hello world!")
#b) Printing Multiple Items
name = "Eswar"
age = 21
print("Name:",name,"Age:", age)
#c) Using sep to Change the Separator
print("2003","09","12",sep="-")
#d) Using end to Control Line Endings
print("Eswar ",end=" ")
print("Ramanjaneyulu")
#Printing Special Characters
#● New Line (\n):
print("Eswar\nRamanjaneyulu")
#● Tab (\t):
print("Eswar\tRamanjaneyulu")
#1️⃣Using Commas (Simple Print Method)
name="Eswar"
age=21
course="python"
print("Name:",name,"Age:",age,"Course:",course)
#2️⃣Using Modulo Operator (% Formatting)
name="Eswar"      #%d=integer
age=21            #%f=float
course="python"   #%s=string
print("Name:%s | Age:%d | Course:%s"% (name,age,course)) 
#3️⃣Using f-strings (Formatted String Literals) — Python 3.6+
name="Eswar"
age=21
course="python"
print(f"Name:{name}|Age:{age}|Score:{course}")
#4️⃣Using str.format() Method
print("Name:{}|Age:{}|Score:{}".format(name,age,course))
