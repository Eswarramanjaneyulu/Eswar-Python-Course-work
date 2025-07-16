print("Hello World!")

#2.1 Empty List
my_list = []
my_list2 = list()

#2.2 List with Elements
number=[1,2,3,4,5,6,7]               # List of integers
fruits=["apple","banana","cherry"]   # List of strings
mixed=[7,"Dhoni",7.0,True]           # Mixed data types
print(number)
print(fruits)
print(mixed)

#2.3 List with Nested Lists
a=[[1,2,3],["a","b","c"],[True,False]]
print(a)

#2.4 List using list() Constructor
a = list((1, 2, 3)) # Converting tuple to list
b = list("Python") # ['P', 'y', 't', 'h', 'o','n']
print(type(a))
print(type(b))
print(a)
print(b)

#3. Accessing Elements in a List

#3.1 Using Indexing (Positive & Negative)
a=["Dhoni","Pawan Kalyan","Prabhas"]
print(a[0])
print(a[1])
print(a[2])
print(a[-1])

#3.2 Using Slicing
a=[1,2,3,4,5,6,7]
print(a[1:4])
print(a[:7])
print(a[2:])
print(a[-3:-1])
print(a[::-1])
print(a[1::])

#4. Modifying Lists
#4.1 Changing Elements
a=[1,2,3,4,5,6,7]
a[2]=10
print(a)

#4.2 Adding Elements
a=[1,2,3,4,5,6,7]
a.append(8)
print(a)
a=[1,2,3,4,5,6,7]
a.insert(8,8)
print(a)
a=[1,2,3,4,5,6,7]
a.extend([8,9,10])
print(a)

#4.3 Removing Elements
a=[1,2,3,4,5,6,7]
a.remove(4)
print(a)
a=[1,2,3,4,5,6,7]
a.pop(2)
print(a)
a=[1,2,3,4,5,6,7]
a.pop()
print(a)
a=[1,2,3,4,5,6,7]
del a[5]
print(a)
a=[1,2,3,4,5,6,7]
a.clear()
print(a)

#5. List Methods
a=[1,2,3,4,5,6,7]
a.append(8)
print(a)
a=[1,2,3,4,5,6,7]
a.extend([8,9,10])
print(a)
a=[1,2,3,4,5,6,7]
a.insert(2,2)
print(a)
a=[1,2,3,4,5,6,7]
a.remove(3)
print(a)
a=[1,2,3,4,5,6,7]
a.pop(3)
print(a)
a=[1,2,3,4,5,6,7]
a.clear()
print(a)
a=[1,2,3,4,5,6,7]
a.index(7)
print(a)
a=[1,1,2,2,4,4,5,5,6,6,3,3,7,7,7,7]
print(a.count(7))
a="eswar ramanjaneyulu"
print(a.count("r"))
a=[7,6,5,4,3,2,1]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
sorted(a)
print(a)

#8. Copying a List
## Shallow Copy
a=[1,2,3,4]
b=a.copy()
print(b)
b.append(5)
print(b)
print(a)

#deep copy
a=[7,8,9,6]
c=a 
print(c)
c.append(5)
print(c)
print(a)

#9. Sorting and Reversing Lists
a=[5,4,3,2,1]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.reverse()
print(a)

a=["eswar","rama","sai"]
a.append("mani")
print(a)
del a[2]
a.pop(0)
print(a)