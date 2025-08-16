
a=[1,2,3,4,5,6]
for i in a:
    print(f"i*{i}={i*i}")

for i in range(0,11):
    print(i)
    
for i in range(2,21,2):
    print(i)

for i in range(1,21,2):
    print(i)

for i in range(20,1,-2):
    print(i)

for i in range(19,1,-2):
    print(i)

a=int(input())
for i in range(1,21):
    print(f"{a}X{i}={a*i}")

a=1
while a<=10:
    print(a)
    a+=1
    
    
email,password="eswar@gmail.com","Eswar@143"

max_attempt=5
current_attempt=1
while current_attempt<=max_attempt:
    e=input("Enter a email: ")
    p=input("Enter a password: ")
    if e==email and p==password:
        print("Login sucessfuly!")
        break
    else:
        print("Incurrect email or password, Try again")
    current_attempt+=1
else:
    print("Max attemptes are completed so your account are Blocked!")