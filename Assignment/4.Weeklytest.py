#1.compute geometric values (math module)
import math
def circle_geometry(radius):
    area= math.pi*radius**2
    circumference= 2*math.pi*radius
    return area,circumference
radius=float(input())
print(circle_geometry(radius))

#2.random team picker(random moudule)
import random
def pick_random_team(members,team_size):
    return random.sample(members,team_size)
members=eval(input())
team_size=int(input())
print(pick_random_team(members,team_size))

#3.Temperature Alert(Lambda+filter)
temp=list(map(int,input().split(',')))
high_temp=list(filter(lambda t:t>40,temp))
print(high_temp)

#4.identify primr number (recursion)
def is_prime(n, divisor=2):

    if n <= 1:
        return False
    if divisor * divisor > n: 
        return True
    if n % divisor == 0:
        return False
    
    return is_prime(n, divisor + 1)

a = int(input("Enter a number: "))
print(is_prime(a))

#.Reverse digits(recursion)
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)

n = int(input("Enter a number: "))
print(reverse_number(n))

#6.filter by starting letter (lambda)
words = eval(input("Enter words separated by commas: "))

letter = input("Enter starting letter: ")

filtered_words = list(filter(lambda w: w.strip().lower().startswith(letter.lower()), words))

print("Words starting with", letter, ":", filtered_words)

#7.create your own utility module(user-defined module)
# string_utils.py  (your utility module)
def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def capitalize_words(s):
    return s.title()
s = input("Enter text: ")
print(is_palindrome(s))        
print(capitalize_words(s))

#8.remove duplicates case-insensitive(set+lambda)
def remove_duplicate(words):
    return set(map(lambda w:w.lower(),words))
words=eval(input())
print(remove_duplicate(words))

# 9.countdown timer(generator)
def count_down(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number: "))
print(*count_down(n), sep=",")    

#10.nested sum (recursion)
def nested_sum(lst):
    total=0
    for item in lst:
        if isinstance(item,list):
            total+=nested_sum(item)
        else:
            total+=item
    return total
lst=eval(input("Enter a list: "))
print(nested_sum(lst))

