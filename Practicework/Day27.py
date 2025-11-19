'''
#OOP, Classes, Objects, Attributes, and Methods
#Classes
# Step 1: Define a class
class product:
    name="Laptop"
    price=50000
    quantity=10
# Methods (functions)
    def display_info(self):
        print(f"Product:{self.name},Price:{self.price},Quantity:{self.quantity}")
#Objects
# Step 2: Create objects of the Product class
product1=product()
product2=product()
#Access attributes and methods
product1.display_info()
product2.display_info()
#Attributes
# Step 3: Modify attributes
product1.name="Smartphone"
product1.price=30000
product1.quantity=7
product1.display_info()

#(a) Instance Attributes
class product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
p1=product("Laptop",50000,10)
p2=product("Smartphone",30000,7)
print(f"Name:{p1.name}") 
print(f"Price:{p1.price}") 
print(f"Quantity:{p1.quantity}")
print(f"Name:{p2.name}") 
print(f"Price:{p2.price}")
print(f"Quantity:{p2.quantity}")
#(b) Class Attributes
class product:
    discount="10%"
    def __init__(self,name,price):
        self.name=name
        self.price=price
print(f"Discount:{product.discount}")

# Method
class product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        
    def display_info(self):
        print(f"Product:{self.name},Price:{self.price},Quantity:{self.quantity}")
        
    def calculate_total_price(self):
        return self.price*self.quantity

product1=product("Tablete",20000,3)
print("Total Price:", product1.calculate_total_price())

#Types of Methods
# (a)Instance Methods
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self, discount):
        self.price -= self.price * (discount / 100)
p1 = Product("Laptop", 50000)
p1.apply_discount(10)
print(p1.price)

#(b) Class Methods
class product:
    discount=10
    @classmethod
    def set_discount(cls, new_discount):
        cls.discount=new_discount
product.set_discount(15)
print(product.discount)

#(c)Static method
class Product:
    @staticmethod
    def is_expensive(price):
        return price > 30000
print(Product.is_expensive(50000)) 
print(Product.is_expensive(20000))

#1. self in Instance Methods
class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display_info(self):
        print(f"product:{self.name},product:{self.price}")
p1=product("Laptop",50000)
p2=product("Phone",20000)

p1.display_info()
p2.display_info()

#2. self Helps in Modifying Instance Attributes
class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def apply_discount(self,discount):
        self.price=self.price*(discount/100)
p1=product("Laptop",50000)
p1.apply_discount(10)
print(p1.price)

#3. self is Not a Keyword
class product:
    def __init__(xyz,name,price):
        xyz.name=name
        xyz.price=price
    def display_info(abc):
        print(f"product:{abc.name},price:{abc.price}")
p1=product("T.V",100000)
p1.display_info()        

#4. self vs. Class Attributes (cls)
class product:
    discount=5
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def apply_discount(self):
        self.price=self.price*(self.discount/100)
        
    @classmethod
    def set_discount(cls,new_discount):
        cls.discount=new_discount
product.set_discount(10)
p1=product("Laptop",50000)
p1.apply_discount()
print(p1.price)

#Constructors
class Product:
# Constructor
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def display_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")
# Create an object
product1 = Product("Headphones", 1500, 10)
product1.display_info()
'''



