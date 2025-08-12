def armstrong():
    print('1')
    print('''
def is_armstrong(num):
    order = len(str(num))
    return num == sum(int(digit) ** order for digit in str(num))
number = int(input("Enter a number: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is NOT an Armstrong number")
    
input: 153
output: 153 is an Armstrong number

Explination: An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
''')
    
    
def  gcd():
    print("2") 
    print('''
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1= int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")

input: num1=12
       num2=18
output:6

Explination: GCD (Greatest Common Divisor) is the largest number that divides two numbers without leaving a remainder — e.g., GCD of 12 and 18 is 6
''')
    
def custom_sort():
    print("3")
    print('''
def custom_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

sorted_list = custom_sort(numbers)
print("Sorted List:", sorted_list)      

input: [5,6,1,2,7,4,3]
output: [1,2,3,4,5,6,7]

Explination: A sorted list arranges elements in ascending (or descending) order
''')
    
def reverse_number():
    print("4")
    print(
'''
def reverse_number(num):
    return int(str(num)[::-1])
    
n = int(input("Enter a number: "))

print("Reversed Number:", reverse_number(n))

input:4321
output:1234

Explination: A reverse number flips the order of its digits 

'''
    )

def sum_of_digit():
    print("5")
    print('''
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))
n = int(input("Enter a number: "))

print("Sum of digits:", sum_of_digits(n))

input: 1234
output:10

Explination:Sum of digits adds all digits of a number — e.g., 1234 → 1+2+3+4 = 10
''')
    
def count_word():
    print("6")
    print('''
def count_words(sentence):
    return len(sentence.split())
text = input("Enter a sentence: ")
print("Word count:", count_words(text))   

input:"Hello World Python" 
output:3

Explination: Word count counts the number of words in a sentence — e.g., "Hello world Python" → 3 words.
''')
    
def title_case():
    print("7")
    print('''
def to_title_case(text):
    return text.title()
text = input("Enter a sentence: ")
print("Title case:", to_title_case(text))

input: "hello world python"
output: "Hello World Python"

Explination: Title case capitalizes the first letter of each word
''')