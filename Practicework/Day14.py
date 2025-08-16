products={
    1:{"name":"Milk","price":30},
    2:{"name":"Curd","price":30},
    3:{"name":"Drink","price":99},
    4:{"name":"Rice bag","price":1500},
    5:{"name":"Wheat","price":60},
    6:{"name":"Sugar","price":42},
    7:{"name":"Chillpowder","price":400},
    8:{"name":"Salt packet","price":20},
    9:{"name":"Turmeric powder","price":50},
    10:{"name":"Sunflower Oil","price":185},
    11:{"name":"Tea powder","price":250}
}
print("<-------------Welcome To Siva Sakthi Kiranashope!-------------->")

for i in range(1,12):
    print(f"{i}. {(products[i] ["name"]).ljust(15," ")}:{products[i] ["price"]}")

items=list(map(int,input("Enter a item indexes: ").split()))
print(items)

total=0
ids=set()
for i in items:
    if i not in ids:
        co=items.count(i)
        total+=(products[i] ["price"]*co)
        print(f"{products[i] ["name"]}-{co}*{products[i] ["price"]} = {products[i] ["price"]*co}")
        ids.add(i)
        
print("Total Bill:",total)
print("Thank you for shopping with us!")