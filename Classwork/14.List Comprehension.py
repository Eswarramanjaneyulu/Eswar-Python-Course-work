#1. What is a List?
'''
numbers=list(input("Enter a numbers: "))
names=list(input("Enter a names: "))
mixed=list(input("Enter a mixed: "))
print(type(numbers))
print(type(names))
print(type(mixed))
print(numbers)
print(names)
print(mixed)

#2.List Comprehension?
# syntx of [expression for item in iterable if condition]
#a. Square numbers in a range:
a=int(input())
squares=[x*x for x in range(a)]
print(squares)

def squares(a):
    return [x*x for x in range(a)]
a=int(input())
print(squares(a))

#b. Filter even numbers:
numbers = list(map(int,input().split()))
evens = [n for n in numbers if n % 2 == 0]
print(evens)

def even_numbers(numbers):
    return [a for a in numbers if a%2==0]
numbers=list(map(int,input().split()))
print(even_numbers(numbers))

#c. Uppercase a list of strings:
names=eval(input())
upper_names=[name.upper() for name in names]
print(upper_names)

def upper_case(names):
    return [name.upper() for name in names]
names=eval(input())
print(upper_case(names))

#5. Create Lists and Apply List Comprehensions
products=eval(input("Enter a proiducts: "))
user_products = [p.upper() for p in products]
print(user_products)

def products(user_products):
    return [p.upper() for p in user_products]
User_products=eval(input())

print(products(User_products))

#List 2: Prices (numbers)  Apply 10% discount
prices=list(map(int,input().split()))
discounted = [price-(price*0.1) for price in prices]
print(discounted)

def prices(price):
    return [price-(price*0.1) for price in price]
price=list(map(int,input().split()))
print(prices(price))

#List 3: Stock status (boolean)
in_stock = eval(input())
a=[i for i, stock in enumerate(in_stock) if stock]
print(a)

def in_stock(a):
    return [i for i, stock in enumerate(a) if stock]
a=eval(input())
print(in_stock(a))

#List 4: Product info as tuples
a=eval(input())
b=[name for name, price in a if price>700]
print(b)

def product_info(names):
    return [name for name, price in names if price>700]
names=eval(input())
print(product_info(names))

#List 5: List of dictionaries
products_data=[
    {"name":"Laptop","price":1000,"stock":3},
    {"name":"Mobile","price":800,"stock":0},
    {"name":"Tablets","price":450,"stock":5}
]

availables_names =[p["name"] for p in products_data if p["stock"]>0]
print(availables_names)

def produts(products_data):
    return [p["name"] for p in products_data if p["stock"]>0]
products_data=[
            {"name":"Laptop","price":1000,"stock":3},
            {"name":"Mobile","price":800,"stock":0},
            {"name":"Tablets","price":450,"stock":5}
        ]
print(produts(products_data))
#Get discounted prices for products in stock
products_data=[
    {"name":"Laptop","price":1000,"stock":3},
    {"name":"Mobile","price":800,"stock":0},
    {"name":"Tablets","price":450,"stock":5}
]
discounted_products = [{p["name"]: p["price"]-(p["price"]*0.1)} for p in products_data if p["stock"] > 0]
print(discounted_products)

def produts(products_data):
    return [{p["name"]: p["price"]-(p["price"]*0.1)} for p in products_data if p["stock"] > 0]
products_data=[
            {"name":"Laptop","price":1000,"stock":3},
            {"name":"Mobile","price":800,"stock":0},
            {"name":"Tablets","price":450,"stock":5}
        ]
print(produts(products_data))
'''
