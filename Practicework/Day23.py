# Check if a Number is Armstrong using for loop

num = int(input("Enter a number: "))

# Convert number to string to count digits
n = len(str(num))
sum_of_powers = 0

# Copy number for calculation
temp = num

for digit in str(num):   # iterate over each digit
    sum_of_powers += int(digit) ** n

if sum_of_powers == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

 