'''#recursive function:
n=input("Enter the number: ")
sum=0
for i in n:
    sum +=int(i)
    print(sum)   
    
n=int(input("Enter a value: "))
def sumofdigits(n):
    if n==0:
        return 0
    return n%10+sumofdigits(n//10)
print(sumofdigits(n))

n=int(input("Enter a number: "))
a=0 
b=1 
if n==1:
    print(a)
elif n>=2:
    print(b)

    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c

#Pattern Problems Using Nested Loops
print("Square Pattern")
a=5
for i in range(a):
    for j in range(a):
        print("*",end=" ")
    print()

print("Right-Angled Triangle")
a=5
for i in range(a):
    for j in range(i+1):
        print("*",end=" ")
    print()
   
print("Inverted Right-Angled Triangle") 
a=5
for i in range(a,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print("Pyramid Pattern")
n = 5 
for i in range(n):
    print(' ' * (n -i -1) + '* ' *(i + 1))
        
print("Diamond Pattern")     
n = 5
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))  

for i in  range (n-2,-1,-1):
    print(' ' * (n-i-1)+'* '*(i+1))

print("Number Triangle")
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print() 

for i in range(0,10):
    print(i)   
    
for i in range(0,10,2):
    print(i)  

a=[1,2,3,4,5]
for i in a:
    print(i)  

a="eswar"
for i in a:
    print(i)

k=10
while k<20:
    print("eswar")
    k+=1

import sys
import platform
import math
import random
import collections

import platform

print(platform.system())
print(platform.version())
print(platform.processor())

import math

print(math.sqrt(25))
print(math.pow(3,2))
print(math.fabs(-7))
print(math.floor(7.5))
print(math.ceil(24.1))
print(math.tan(90))
print(math.sin(90))
print(math.cos(90))
print(math.degrees(7))

import random

print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))
l=["eswar","mani","aditya","venky","sai","chaitu","krishna"]
print(random.choice(l))
print(random.choices(l,k=3))
random.shuffle(l)
print(l)

import collections

names=["maha","lakshmi","surya","sudha","kusuma","vidya","vidya","vidya","maha","sudha","maha"]
c=collections.Counter(names)
print(c)

import collections

names="python programming"
d={}
for i in names:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


import collections

names="python programming"
d=collections.defaultdict(int)
d['p']+=1
print(d)

import random

player1_score=0
player2_score=0

while player1_score<100 or player2_score<100:
    player1_turn=random.randint(1,6)
    player1_score+=player1_turn
    print(f"\nplayer1 score:{player1_score}-Dice:{player1_turn}\n")
    
    player2_turn=random.randint(1,6)
    player2_score+=player2_turn
    print(f"\nplayer2 score:{player2_score}-Dice:{player2_turn}\n")
    
if player1_score>player2_score:
    print(f"\nplayer1 Win")
elif player1_score<player2_score:
    print(f"\nplayer2 Win")
else:
    print("Tie")
    

import random

player1_score=0
player2_score=0

while player1_score<100 and player2_score<100:
    player1=input("player1 -[s]top and [c]ontinue:")
    if player1=='c':
        player1_turn=random.randint(1,6)
        player1_score+=player1_turn
        print(f"\nplayer1 score:{player1_score}-Dice:{player1_turn}\n")
    else:
        print("player2 Win")
        break
    player2=input("player2 -[s]top and [c]ontinue:")
    if player2=='c':
        player2_turn=random.randint(1,6)
        player2_score+=player2_turn
        print(f"\nplayer2 score:{player2_score}-Dice:{player2_turn}\n")
    else:
        print("player1 Win")
if player1_score>player2_score:
    print(f"\nplayer1 Win")
elif player1_score<player2_score:
    print(f"\nplayer2 Win")
else:
    print("Tie")

import random

player1_score=0
player2_score=0
snakes ={19:6,25:11,39:7,50:25,75:18,80:45,98:2}
ladders={7:79,9:22,17:69,55:76,70:98}
while player1_score<100 and player2_score<100:
    player1=input("player1 -[s]top and [c]ontinue:")
    if player1=='c':
        player1_turn=random.randint(1,6)
        player1_score+=player1_turn
        if player1_score in snakes:
            player1_score=snakes[player1_score]
            print(f"\n---------player1-snake bit -score:{player1_score}-Dice:{player1_score}\n")
        elif player1_score in ladders:
            player1_score=ladders[player1_score]
            print(f"\n**********player1-ladder-score:{player1_score}-Dice:{player1_score}\n")
        else:
            print(f"\nplayer1 score:{player1_score}-Dice:{player1_turn}\n")
    else:
        print("player2 Win")
        break
    player2=input("player2 -[s]top and [c]ontinue:")
    if player2=='c':
        player2_turn=random.randint(1,6)
        player2_score+=player2_turn
        if player2_score in snakes:
            player2_score=snakes[player2_score]
            print(f"\n---------player2-snake bit -score:{player2_score}-Dice:{player2_score}\n")
        elif player2_score in ladders:
            player2_score=ladders[player2_score]
            print(f"\n**********player2-ladder-score:{player2_score}-Dice:{player2_score}\n")
        else:
            print(f"\nplayer2 score:{player2_score}-Dice:{player2_turn}\n")
    else:
        print("player1 Win")
if player1_score>player2_score:
    print(f"\nplayer1 Win")
elif player1_score<player2_score:
    print(f"\nplayer2 Win")
else:
    print("Tie")

a=int(input("Enter a num1: "))
b=int(input("Enter a num2: "))
c=int(input("Enter a num3: "))
if a==b and a==c and c==b:
    print("Equilateral")
elif a==b and a!=c and b!=c:
    print("Isosceles")
else:
    print("Scalene")

a=input("Enter a char1: ")
vowel="aeiouAEIOU"
if a.isalpha(): 
    if a in vowel:
        print("It's a Vowel")
    else:
        print("It's a consonant")
elif a.isdigit():
    print("It's a Digit")
else:
    print("It's a special")

a=float(input("Enter a height: "))
b=float(input("Enter a weight: "))
bmi=b/(a*a)

if bmi>25:
    print("overweight")
elif bmi<25:
    print("Underweight")
else:
    print("perfact")

a=int(input("Enter a bill: "))
bill=0
if a<=100:
    bill=a*1
elif a>100 and a<=200:
    bill=100*1+(a-100)*2
else:
    bill=100*1+100*2+(a-200)*3
    
print(bill)
'''

class shopping:
    discount=10
    
    classmethod
    def update(cls,new_discount):
        cls.discount=new_discount
        print(f"{new_discount} is updated")
        
    def product(self,price,name):
        self.price=price
        self.name=name
              
user1=shopping()
user2=shopping()

user1.product(34000,'laptop')
user2.product(15000,'phone')

print(shopping.discount)
shopping.discount=15
print(user1.price)
