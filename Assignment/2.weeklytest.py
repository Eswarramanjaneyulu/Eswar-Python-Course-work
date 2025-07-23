#Automated salary tax Calculator
a=float(input("Enter a salary: "))
if a > 250000 and a <= 500000:
    print(a*0.05)
elif a > 500000 and a <= 1000000:
    print(a*0.2)
elif a > 1000000:
    print(a*0.3)
else:
    print("No Tax")

#Movie Ticket pricing 
a=int(input("Enter a members: "))
total=0
for _ in range(a):
    b=int(input("Enter a Age: ")) 
    if b>=a and b<=18:
        total+=100
    elif b>=19 and b<=60:
        total+=150
    elif b>60:
        total+=120
print(total)

#Electricity bill generator'
a=int(input("Enter a units: "))
bill = 0
if a<=100:
    bill+=a*1.5
elif a>100 and a<=200:
    bill+=150+(a-100)*2.5
elif a>200 and a<=500:
    bill+=400+(a-200)*4
else:
    bill+=1600+(a-500)*6
print(bill)

#car parking feee calculator
a=int(input("Enter a time: "))
if a<=2:
    print("30 rupees")
elif a>2 and a<=24:
    c=(a*10)+10
    print(c)
else:
    print("200 rupees")

#product inventory checker
a=input("Enter a product: ")
b=int(input("Enter a quantity: "))
if b==0 :
    print(a,": out of stock")
elif b>=1 and b<=10:
    print(a,": low stock")
elif b>=11 and b<=50:
    print(a,": in stock")
else:
    print(a,": over stock")

#pattern 0 and 1
a=int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        print((i+j)%2,end=" ")
    print()

#Gym subscription billing
choice=int(input("Enter a data: "))
people = int(input("Enter a members:"))
if choice==1:
    print(people*500)
elif choice==2:
    print(people*1300)
elif choice==3:
    print(people*5000)

#Billing Bot -Apply Discount Based on Amount
a=int(input("Enter a Bill: "))
if a>=1000 and a < 5000:
    print(a-a*0.05)
elif a>=5000 and a<10000:
    print(a-a*0.1)
elif a>=10000:
    print(a-a*0.15)
else:
    print(a)

#ATM pin
currect_pin="1234"
attempts = 0
max_attempts =3

while attempts<max_attempts:
    entered_pin =input("Enter your pin: ")
    if entered_pin == currect_pin:
        print("Access Granted")
        break
    else:
        print("Incurrect pin. try agin")
        attempts +=1
else:
    print("ATM Blocked.try Again later")

#Bus booking System-track Full and Empty Seats
a=int(input("Enter a total seats: "))
b=list(map(int,input("Enter a booked seats: ").split()))
print(f'Total Seats:{a}')
print(f'Booked Seats:{len(b)}')
print(f'Available Seats:{a-len(b)}')