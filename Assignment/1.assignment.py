'''
class Mini_Flipkart:
    
 product_id = int(input("Enter Product ID: "))
 product_name = input("Enter Product Name: ")
 product_price = float(input("Enter Product Price: "))
 product_category = input("Enter Product Category: ")
 available_stock = int(input("Enter Available Stock: "))
 sold_stock = int(input("Enter Sold Stock: "))
 discount_percentage = input("Enter Discount Percentage: ")
 product_features = input("Enter Product Features: ")

 print("\nProduct Details:")
 print("ID:", product_id)
 print("Name:", product_name)
 print("Price: ₹", product_price)
 print("Category:", product_category)
 print("Available Stock:", available_stock)
 print("Sold Stock:", sold_stock)
 print("Discount:", discount_percentage)
 print("Features:", product_features)
'''
class Mini_Flipkart:
    def __init__(self, product_id, product_name, product_price, product_category,
                 available_stock, sold_stock, discount_percentage, product_features):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_category = product_category
        self.available_stock = available_stock
        self.sold_stock = sold_stock
        self.discount_percentage = discount_percentage
        self.product_features = product_features

    def display_product_details(self):
        print("\nProduct Details:")
        print("ID:", self.product_id)
        print("Name:", self.product_name)
        print("Price: ₹", self.product_price)
        print("Category:", self.product_category)
        print("Available Stock:", self.available_stock)
        print("Sold Stock:", self.sold_stock)
        print("Discount:", self.discount_percentage)
        print("Features:", self.product_features)


# Taking input from the user
pid = int(input("Enter Product ID: "))
pname = input("Enter Product Name: ")
pprice = float(input("Enter Product Price: "))
pcategory = input("Enter Product Category: ")
astock = int(input("Enter Available Stock: "))
sstock = int(input("Enter Sold Stock: "))
discount = input("Enter Discount Percentage: ")
pfeatures = input("Enter Product Features: ")

# Creating object
product = Mini_Flipkart(pid, pname, pprice, pcategory, astock, sstock, discount, pfeatures)

# Displaying details
product.display_product_details()


