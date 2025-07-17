
'''   
email = "eswar@gmail.com"
password = "Eswar@143"
max_attempt=5
cur_attempt=1

while cur_attempt <= max_attempt:
    email=input("enter the email: ")
    password=input("enter the password: ")
    
    if email == email and password == password:
        print("LOgin Successful!")
        break
    else:
        cur_attempt -= 1
        print(f"Incorrect creadentials.Attempts lesft:{cur_attempt}")
else:
    print("Too many failed attempts.Access blocked")


num = int(input("Enter a number: "))

# Check if number is prime
if num > 1:
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    # Find the position of the prime number
    count = 0
    for i in range(2, num + 1):
        prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                prime = False
                break
        if prime:
            count += 1
    print(f"{num} is a Prime number and it is the {count} prime number.")
else:
    print(f"{num} is NOT a Prime number.")
'''
n=int(input("Enter the no of messages: "))
chat={}
