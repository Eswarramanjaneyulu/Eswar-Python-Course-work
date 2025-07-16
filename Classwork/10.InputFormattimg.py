#1. String Input
name = input("Enter your name: ")
print(name)

#2. Integer Input
i = int(input("Enter the number: "))
print(i)

#3. Float Input
f = float(input("Enter the price: "))
print(f)

#4. Input as List (Space-separated)
name = input("Enter employee names (space-separated):").split()
print(name)

#5. Input as List (Comma-separated)
tags = input("Enter tags (comma-separated): ").split(',')
print(tags)

#list of integers
marks = list(map(int,input("enter marks: ").split()))
print(marks)

#list of float
weights = list(map(float, input("Enter weights: ").split()))
print(weights)

#tuple input
dimensions = tuple(map(int, input("Enter length, width,height: ").split()))
print(dimensions)

#9. Set Input
selected_ids = set(map(int, input("Enter selected image IDs:").split()))
print(selected_ids)

#10. Dictionary Input using eval()
profile = eval(input("Enter user profile as a dictionary: "))
print(profile)

#11. Multiple Inputs with Unpacking
username, password = input("Enter username and password:").split()
print("Username:", username)
print("Password:", password)
