#Basic Examples of print()
# a) Printing Text
print("Hello,World!")

# b) Printing Multiple Items
name = "eswar"
age = 22
print("name:",name,"age:",age)

# c) Using sep to Change the Separator
print("2003","09","12",sep="/")

# d) Using end to Control Line Endings
print("Hello,",end=" ")
print("World!")

#Printing Special Characters
#● New Line (\n):
print("Eswar\nRamanjaneyulu")
#● Tab (\t):
print("Nmae:Chodisetti\tEswar\tRamanjaneyulu")

#Output Formatting
#1️⃣Using Commas (Simple Print Method)
name="Eswar"
age=22
course="python"
print("Name:",name,"Age:",age,"Course:",course)

#2️⃣Using Modulo Operator (% Formatting)
name="Eswar"
age=22
course="python"
print("Name: %s | Age:%d | Course: %s" % (name,age,course))

#3️⃣Using f-strings (Formatted String Literals) — Python 3.6+
name = "Eswar"
age = 22
course = "python"
score = 65.91
print(f"Name:{name} | Age:{age} | Course:{course} | Score:{score:.2f}")

#4️⃣Using str.format() Method
name = "Eswar"
age = 22
course = "python"
score = 65.91
print("Nmae: {} | Age:{} | Score:{:.1f} | Course:{}".format(name,age,score,course))

