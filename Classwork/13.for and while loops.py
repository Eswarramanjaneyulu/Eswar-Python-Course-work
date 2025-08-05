#FOR LOOP
'''
a=list(map(int,input("Enter a numbers: ").split()))
current_streak =0
longest_streak =0

for day in a:
    if day ==1:
        current_streak += 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak=0
print("Longest workout streak: ",longest_streak)

# for loop
correct_pin ="143143"
attempts = 0
max_attempts = 3

for login in correct_pin:
    entered_pin =input("Enter your pin: ")
    if entered_pin == correct_pin:
        print("Login successful.")
        break
    else:
        print("Incorrect pin. Try agin.")
        attempts +=1
else:
    print("Account locked due to too many failed attempts.")

# while loop
correct_pin ="143143"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_pin =input("Enter your pin: ")
    if entered_pin == correct_pin:
        print("Login successful")
        break
    else:
        print("Incorrect pin. Try agin.")
        attempts +=1
else:
    print("Account locked due to too many failed attempts.")

#FOR LOOP WITH ELSE
a = list(input("Enter a data: "))
for i in a:
    if i==1:
        print("You have unread notifications!")
        break
else:
    print("All caught up!")

#WHILE LOOP WITH ELSE
correct_OTP="9014"
attempts=0
max_attempts=3
while attempts<max_attempts:
    enter_OTP=input("Enter your OTP: ")
    if enter_OTP==correct_OTP:
        print("OTP VERIFICATION SUCCESSFULL")
        break
    else:
        print("OTP incorrect,Try again!")
        attempts+=1
else:
    print("Your OTP experied. Request a new one")
'''
#break Statement in Python
#syntx
'''for iteam in iterable:     while condition:
    if condition:         or       if exit_condition:
        break                       break'''
'''
numbers = list(map(int,input("Enter a numbers: ").split()))
target = int(input("Enter a target num: "))
for num in numbers:
    if num == target:
        print("Target found:", num)
        break   
else:
    print("Target not found")  

#continue Statement in Python
# Print odd numbers only
for num in range(1,10):
    if num % 2 == 0:
        continue
    print(num)

#Nested Loops
for i in range(2):
    for j in range(1):
        print(f"i={i},j={j}")

#1. Square Pattern
print("Square Pattern").center(50,)
n=int(input("Emter a number: "))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

#2. Right-Angled Triangle
n=int(input("Emter a number: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

#3. Inverted Right-Angled Triangle
print("Inverted Right-Angled Triangle".center(50," "))
n=int(input("Emter a number: "))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#4. Pyramid Pattern
print("pyramid pattern".center(20," "))
a=int(input("Enter a number: "))
for i in  range(a):
    print(' '* (a-i-1)+"* "*(i+1))

#5.Pyramid Pattern
print("Inverted  Pyramid Pattern ".center(20," "))
a=int(input("Enter a NUMBER: "))
for i in range(a- 2, -1, -1):
    print(' ' * (a- i - 1) + '* ' * (i + 1))

#5. Diamond Pattern
print(" Diamond Pattern".center(20," "))
a=int(input("Enter a number: "))
for i in range(a):
    print(' '* (a-i-1)+'* '*(i+1))
    
for i in range(a-2,-1,-1):
    print(' '*(a-i-1)+'* '*(i+1))
'''
    
