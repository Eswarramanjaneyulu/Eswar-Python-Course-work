#Control Statements
#FOR LOOP
'''
fruits=["apple","bananna","cherry"]
for i in fruits:
    print(i)
    
# using for with if condition inside (loop)
for num in range(1,11):
    if num%2==0:
        print("even")
    else:
        print("odd")
'''
currect_pin="143143"
attempts = 0
max_attempts =3

while attempts<max_attempts:
    entered_pin =input("Enter your pin: ")
    if entered_pin == currect_pin:
        print("Login successful")
        break
    else:
        print("In currect pin. try agin")
        attempts +=1
else:
    print("your account is blocked due to many failed attempts")