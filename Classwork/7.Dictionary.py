print("Hello World!")

#1. Introduction to Dictionary
#ictionary_name = {key1: value1, key2: value2, key3: value3}

a={"name":"Dhoni","age":45,"course":"railway","skills":"he is cricket player"}
print(a)

#2. Dictionary Operations
#2.1 Accessing Values
print(a["name"])
print(a.get("age"))
print(a["age"])
print(a.get("gender"))

#2.2 Adding and Updating Items
a["city"]="Ranchi"
a["gender"]="male"
print(a)

#2.3 Removing Items from a Dictionary
#Using pop(key)
age=a.pop("age")
print(age)
a={"name":"Dhoni","age":45,"course":"railway","skills":"he is cricket player"}
print(a)
a.pop("age")
print(a)
#Using del
del a["course"]
print(a)
#Using popitem()
a={"name":"Dhoni","age":45,"course":"railway","skills":"he is cricket player"}
a.popitem()
print(a)
#Using clear()
a.clear()
print(a)

#3. Dictionary Built-in Methods
#3.1 Dictionary Methods for Accessing Data
a={"name":"Dhoni","age":45,"course":"railway","skills":"he is cricket player"}
print(a.get('name','not found'))
print(a.keys())
print(a.values())
print(a.items())

#3.2 Dictionary Methods for Adding and Updating Data

a={"name":"Dhoni","age":45,"course":"railway","skills":"he is cricket player"}
a.update({"city":"Ranchi"})
print(a)
print(a.setdefault("city","unknow"))

#3.3 Dictionary Methods for Removing Data
a={"name":"Dhoni","age":45,"course":"railway","skills":"he is cricket player"}
a.pop("age")
print(a)
a.popitem()
print(a)
del a["name"]
print(a)
a.clear()
print(a)

#4. Built-in Functions for Dictionaries
a={"name":"eswar","age":"21","gander":"male","course":"python full stack","city":"kajuluru"}
print(len(a))
print(max(a))
print(min(a))
print(sorted(a))

#5. Nested Dictionaries
students ={ "eswar":{"age":21,"course":"python full stack"},"mani":{"age":20,"course":"data anlysis"} }

print(students["eswar"]["age"])
print(students["eswar"]["course"])
print(students["mani"]["age"])
print(students["mani"]["course"])