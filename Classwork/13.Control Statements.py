#FOR LOOP
'''
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
'''

v=input()
a=v.replace('a','*')
a=v.replace("e","*")
a=v.replace("i","*")
a=v.replace("o","*")
a=v.replace("u","*")
print(a)
     