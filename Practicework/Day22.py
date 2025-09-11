'''
#1.question
try:
    a=int(input("Enter a number: "))
    b=int(input("Emter a number: "))
    result =a/b
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(result)
    

#2 question
try:
    numbers = list(map(int,input("Enter a list: ").split(',')))
    index = int(input("Enter index: "))  
    print("Element at index:", numbers[index])
except IndexError:
    print("Index out of range")
except ValueError:
    print("Please enter a valid integer")

#3 question
import re

text = input("Enter text: ")

pattern = r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}'

emails = re.findall(pattern, text)

if emails:
    print("Extracted Emails:", emails)
else:
    print("No emails found.")

#4 question
import re
number =input("Enter a phone no: ")
pattern =r'\b[6-9]\d{9}\b'

phone_number =re.findall(pattern,number)
if phone_number:
    print("Valid  mobile number")
else:
    print("Invalid mobile Number")

# 5 question
import pandas as pd
marks=eval(input("Enter a data: "))
cutoff=int(input("Enter a cutoff murks"))
b=pd.read_csv(marks)
c=b[b["marks"]>cutoff]
print("Students marks >80")
print(c)

#6 question
import matplotlib.pyplot as plt

months = input("Enter months separated by space: ").split()
sales = list(map(int, input("Enter sales separated by space: ").split()))

plt.bar(months, sales)

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")

plt.show()

import pandas as pd
names,marks={
    "names":"Eswar","marks":75,
    "names":"mani","marks":99,
    "names":"aditya","marks":95,
    "names":"sai","marks":80
}
cutoff=80
b=pd.read_csv(marks)
c=b[b["marks"]>80]
print("Students marks >80")
print(c)

import pandas as pd
# Example: Product Prices
product_prices = pd.Series(
[2999, 15999, 52999, 4999, 1999],
index=["Wireless Earbuds", "Smartphone", "Laptop",
"Smartwatch", "Bluetooth Speaker"]
)
print(product_prices)
data = {
"Product": ["Wireless Earbuds", "Smartphone", "Laptop",
"Smartwatch", "Bluetooth Speaker"],
"Brand": ["SoundMax", "TechNova", "ByteCore", "TimeTrack",
"EchoBoom"],
"Price": [2999, 15999, 52999, 4999, 1999],
"Stock": [50, 30, 20, 40, 60]
}
df = pd.DataFrame(data)
print(df)
'''
