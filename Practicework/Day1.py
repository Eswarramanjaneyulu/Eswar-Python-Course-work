#print("Hello")
#String
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
sum =num1+num2
print("sum:",sum,sep="")
print(f"sum:{num1+num2}")

r=int(input("Enter a radius: "))
print("Areas of the circle:",3.14*r*r,sep="")
print(f"Areas of the circle:{3.14*r*r}")

for row in range(5):
    for col in range(5-row-1):
        print(' ',end='')
    for coll in range(row+1):
        print("*",end='')
    print() 
   
a= input().split('-')
a=a[::-1]
print('/'.join(a))

date,month,year=input().split('-')
print(f"{date}/{month}/{year}")


v=input()
a=v.replace('a','*')
a=v.replace("e","*")
a=v.replace("i","*")
a=v.replace("o","*")
a=v.replace("u","*")
print(a)

username,password ="eswar@gmail.com","Eswar@143"
a,b="username","password"

a=input("Enter a username: ")
b=input("Enter a password: ")

if a==username and b==password:
        print("Login successful!")
else:
        print("not access")
 
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
d=(b**2)-4*a*c
root1=(-b+(d**(1/2)))/2*a
root2=(-b-(d**(1/2)))/2*a
print(f"roots:{root1},{root2}")

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=a 
a=b 
b=c
print(f"value of a is :{a}")
print(f"value of b is :{b}")

def function_name(a):
    return f"hello,{a}!"
print(function_name("Eswar"))

a=input()
print(list(a))

data ={"balance":10000,"history":[]}
def current_blance():
    print(f"{data['balance']}")

def deposit(amount):
    amount=int(input("Enter a amount: "))
    data['balance']+=amount
    data['history'].append(f"withdraw-(amount)")
    print(f"withdraw-{amount}")

def withdraw(amount):
    amount=int(input("Enter a amount: "))
    if amount<=data['balance']:
        data ['balance']-=amount
        data['history'].append(f"withdraw-{amount}")
        print(f"withdraw-{amount}")
    else:
        print("Invaild blance")
        
def histtory():
    if histtory:
        print()
        
#list
a=[1,2,3,4,5,6,7]
b=["apple","bunny","tables"]
c=[7,"dhoni",7.0,True]
print(a)  
print(b)  
print(c)
print(type(a))  
print(type(b))  
print(type(c))  


a=[[1,2,3,4,5,6,7],["apple","bunny","tables"],[7,"dhoni",7.0],[True,False]]
print(a)
print(type(a))


a=(1,2,3)
b="dhoni"
print(list(a))
print(list(b))


a=["eswar","mani","aditya","venky"]
b=[1,2,3,4,5,6,7]
print(a[2])
print(b[5])
print(a[-2])
print(b[-2])


a=["eswar","mani","aditya","venky"]
b=[1,2,3,4,5,6,7]
print(a[1:])
print(b[1:5])
print(b[:5])
print(a[:-3])
print(b[:-5])
print(a[-3:-1])
print(b[-3:-1])
print(a[::-1])
print(b[::-1])


a=[1,2,3,4,5,6,7]
a[5]=7
print(a)

#adding elements
a=[1,2,3,4,5,6,7]
a.append(33)         #adds to the ends
print(a)
a.insert(2,18)       #adds at a specific position
print(a)
a.extend([10,45,8])  #add multiple elements
print(a)


#removing elements
a=[1,2,3,4,5,6,7]
a.remove(4)         #remove the elements
print(a)
a.pop(2)            #remove the index of elements
print(a)
a.pop()             #remove the last elements
print(a)
del a[2]           # deletes the index of elements
print(a)
a.clear()          # llear the all list
print(a)

a=[7,2,3,1,5,6,4]
print(a.index(5))
a.sort()          #we print in  assigning order
print(a)
a.reverse()       # we print in revers  order
print(a)
print(a.count(5)) # we wil print hoe many repirted valus

a=[7,2,3,1,5,6,4]
b=a.copy()        #copy element in another variable
print(b)
a.sort()          # we print in assigning order
print(a)
a=[7,2,3,1,5,6,4]
a.sort(reverse=True) #  we print in descending order
print(a)
print(max(a))        # bigest number of in your list
print(min(a))        # bigest number of in your list
print(sum(a))        # add all elements in your list
print(len(a))        # Returns the number of elements in the list
print(any(a))
print(all(a))

