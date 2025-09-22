'''
my_set={"Eswar","Mani","Aditya",True,100,100}
print("Eswar" in my_set)
print("Eswar" not in my_set)

set1={1,2,3}
set2={3,4,5}
print(set1|set2)
print(set1.union(set2))
print(set1&set2)
print(set1.intersection(set2))
print(set1-set2)
print(set1.difference(set2))
print(set1^set2)
print(set1.symmetric_difference(set2))
print(set1<=set2)
print(set1.issubset(set2))
print(set1>=set2)
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))

my_set={1,2,3,4,5,6}
my_set.add(6)
print(my_set)
my_set.remove(2)
print(my_set)
print(len(my_set))
print(max(my_set))
print(min(my_set))
print(sorted({4,5,2,3,1}))
print(sum(my_set))
print(set([1,2,3,4]))

set1=frozenset([1,2,3,4])
print(set1)

my_dict={
    "Name":"Eswar",
    "Age":22,
    "Gender":"Male",
    "Mobile":9014584004,
    "City":"Kajuluru"
}
print(my_dict)
print(my_dict["Name"])
my_dict["Age"]=23
print(my_dict)
my_dict.update({"City":"Hyd"})
print(my_dict)
my_dict["Street"]="Nunna Vari Street"
print(my_dict)
my_dict.update({"Course":"Python"})
print(my_dict)
my_dict.pop("Course")
print(my_dict)
my_dict.popitem()
print(my_dict)
del my_dict["City"]
print(my_dict)
my_dict.clear()

my_dict={
    "Name":"Eswar",
    "Age":22,
    "Gender":"Male",
    "Mobile":9014584004,
    "City":"Kajuluru"
}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
if "course" in my_dict:
    print("Yes")
else:
    print("No")

print("Exame Result")
marks=int(input())
if marks==35:
    print("You just passed the exam!")
elif marks>35:
    print("You passed Exam!")
    if marks>=35 and marks<55:
        print("You got E grade!")
    elif marks>=55 and marks<65:
        print("You got D grade!")
    elif marks>=65 and marks<75:
        print("You got C geade!")
    elif marks>=75 and marks<85:
        print("You got B grade!")
    elif marks>=85:
        print("You got A grade!")
else:
    print("You failed the exam")

product=int(input())
if product==0:
    print("Out of stock")
elif product<50:
    print("stock in limited ")
else:
    print("stock is available")
    
amazon_stock=int(input())
coupon=input().lower()
prime_member=input().lower()
if amazon_stock >0:
    print("Stock is available!")
    if coupon=="yes" and prime_member=="yes":
        print("You are eligible for a special discount!")
    elif prime_member=="yes":
        print("You are eligible for prime member, but no special discount!")
    elif coupon=="yes":
        print("You are eligible for special discount, but not prime member!")
    else:
        print("Not available for discount!")
else:
    print("Stock is not available!")

a=int(input())
if a==0:
    print("Give number is zero")
elif a>0:
    print("Given number is positive")
else:
    print("Given number is negitive")

a=1
while a<6:
    print(a, "Eswar")
    a+=1

a=1
while a<11:
    print(a, "Eswar")
    if a==7:
        print("a is 7 now ")
        break
    a+=1

a=0
while a<10:
    a+=1
    if a==7:
        print("a is 7 now ")
        continue
    print(a, "Eswar")

for i in range(0,11,2):
    print(i)

persons=["Eswar","Mani","Aditya","Sai"]
for user in persons:
    print(user)

persons=["Eswar","Mani","Aditya","Sai"]
for user in persons:
    print(user)
    if user == "Mani":
        break

persons=["Eswar","Mani","Aditya","Sai"]
for user in persons:
    if user == "Mani":
        continue
    print(user)    

workout_log=list(map(int,input().split()))
current_streak=0
longest_streak=0
for day in workout_log:
    if day==1:
        current_streak+=1
        if current_streak>longest_streak:
            longest_streak=current_streak
    else:
        current_streak=0
print("Longest workout streak:",longest_streak)

currect_pin="Eswar@143"
attempt=0
max_attempt=3

while attempt <max_attempt:
    entered_pin=input("Enter a pin: ")
    if entered_pin == currect_pin:
        print("Login Sucessful!")
        break
    else:
        print("Incorrect pin. Try again")
        attempt+=1
else:
    print("Account locked due to too many failed attempts")
'''
        

