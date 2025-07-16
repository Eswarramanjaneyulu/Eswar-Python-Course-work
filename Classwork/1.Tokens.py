print("Hello World!")

#tokens
length = 10              #length,-id
width = 5                #width,area-id
area = length * width    #=,*,>-op
if area > 30:            #5,10,30,"learg area","small area"-li
  print("Large area")    #if,else-kw
else:                    #:-pun
  print("Small area")    #print()-id
  
#keywords
import keyword

print(keyword.kwlist) 
print(len(keyword.kwlist))

#identifier

name="eswar"
Age=21
_gender="male"


#variables start with a capital latters and small letters and underscore
product_name = "Laptop"
price = 45000
in_stock = True
print(product_name, price, in_stock)


#Multiple Assignment
a, b, c = 10, 20, 30
print(a, b, c)

x = y = z = 100
print(x, y, z)

#Reassignment
x = 5
x = 10
print(x)

#swapping
a, b = 5, 10
a, b = b, a
print(a, b)

#Deleting Variables
x=7
del x

