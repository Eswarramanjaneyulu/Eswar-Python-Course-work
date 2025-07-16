# 1. if Statement
amazon_stock = int(input("Enter a number: "))
if amazon_stock>0:
    print(f'Amazon stock is available!' )
    
# 2. if-else Statement
amazon_stock = int(input("Enter a number: "))
if amazon_stock>0:
    print(f'Amazon stock is available!' )
else:
    print(f'Amazon stock is not available')
    
#3. if-elif-else Statement
amazon_stock = int(input("Enter a number: "))
if amazon_stock > 20:
    print(f"Amazon stock is fully available. ")
elif amazon_stock <= 20 and amazon_stock > 0:
    print(f"Amazon stock is very low ,Hurry up!")
else:
    print(f"Soory, Amazon stock is out of stock.")
    
# 4. Nested Conditional Statements
amazon_stock = int(input("Enter a number: "))
amazon_customer = int(input("Enter a number: "))
if amazon_stock >0:
    print(f"Amazon stock is available")
    if amazon_customer:
        print("Prime customer gets priority shipping!")
    else:
        print("Standard shipping will apply.")
else:
   print("Sorry, Amazon stock is out of stock.")