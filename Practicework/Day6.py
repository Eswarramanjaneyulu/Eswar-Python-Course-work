#Control Statements
#FOR LOOP
fruits=["apple","bananna","cherry"]
for i in fruits:
    print(i)
    
# using for with if condition inside (loop)
for num in range(1,11):
    if num%2==0:
        print("even")
    else:
        print("odd")
#Real-Time Example: Limiting Login Attempts in a Mobile App
currect_pin="143143"
attempts = 0
max_attempts =3

while attempts<max_attempts:
    entered_pin =input("Enter your pin: ")
    if entered_pin == currect_pin:
        print("Login successful")
        break
    else:
        print("Incurrect pin. try agin")
        attempts +=1
else:
    print("your account is blocked due to many failed attempts")
    
#We want to find the longest streak of consecutive workout days.
a=list(map(int,input("Enter a Data: ").split()))
cureent_streak=0
longest_streak=0
for day in a:
    if day == 1:
        cureent_streak += 1
        if cureent_streak>longest_streak:
            longest_streak = cureent_streak
    else:
            cureent_streak = 0
            
print("Longest Workout:",longest_streak)
print("Current Workout:",cureent_streak)

correct_pin = "143143"
attempt = 0
max_attempt = 5

while attempt<max_attempt:
    a=input("Enter a pin: ")
    if a == correct_pin:
        print("Login successful")
        break
    else:
        print("Incorrect PIN. Try again.")
        attempt+=1
else:
    print("Account locked due to too many failed attempts.")

a=input("Enter a wether: ")
if  a=="sunny":
    print("we play cricket")
elif a=="cloudy":
    print("we will play but wait for sometime upto sunny")
elif a=="rainy":
    print("we will play indoor games")
else:
    print("we can sleep")


