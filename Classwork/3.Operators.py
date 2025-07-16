#Arithmetic Operators

a=7
b=7 
print(a+b)   #add two no 14
print(a-b)   #sub two no 0
print(a*b)   #multiplication two no 49
print(a/b)   #division two no 1.0
print(a**b)  #Exponentiation 823543
print(a//b)  #Floor Division 1
print(a%b)   #Modulus 0


#Comparison Operators

a=7 
b=7 
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Assignment Operators

a=7     #7
a+=1    #8
a-=2    #6
a*=3    #36
a**=3   #46656
a/=3    #15552
a//=3   #1728
a%=3    #0.0
print(a)

#Logical Operators
a=7 
b=7 
print(a==b and a<b)  #false
print(a==b or a<b)   #true  
print(not(a==b))     #false

#Membership Operators
a=["eswar","mani","aditya"]
print("eswar" in a)
print("mani" not in a) 
print("venky" in a)
print("venky" not in a)

#Identity Operators
a = [1,2,3]
b = [1,2,3] 
c = a  
print(a is c)
print(a is b)
print(id(a))
print(id(b))
print(id(c))

#Bitwise Operators
a=7           #     32,16,,8,4,2,1
b=8           #0111
print(a & b)  #7
print(a | b)  #15
print(a ^ b)  #0
print(~a)     #-8
print(a << 1) #14
print(a >> 1) #3.5