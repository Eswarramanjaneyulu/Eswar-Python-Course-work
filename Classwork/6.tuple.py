print("Hello World!")



#Tuple

# Empty Tuple
empty_tuple = ()
print(empty_tuple)
# Single-element Tuple (note the trailing comma)
single_tuple = (5,)
print(single_tuple)
# Multi-element Tuple
my_tuple = (1, "apple", 3.5)
print(my_tuple)
# Without parentheses (implicit tuple creation)
implicit_tuple = 1, 2, 3
print(implicit_tuple)

#2. Accessing Tuple Elements
#a. Indexing
a=(1,2,3,4,5,6,7)
print(a[6])
#b. Negative Indexing
print(a[-1])
#slicing
a="sesharao"
print(a[1:6])
print(a[1:8:2])
print(a[0:8:2])

#3. Operations on Tuples
#a. Concatenation
a=(1,2)
b=(7,8)
t=a+b
print(t)
#b. Repetition
print(b*7)
#c. Membership Testing
print(2 in a)
print(7 in a)
print(7 not in a)
print(7 in b)
#d. Tuple Unpacking
x,y=a
z,s=b
print(x,y,z,s)
print(x,y)
print(x)
print(x,s)

#4. Tuple Methods
#count
a=(7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8)
print(a.count(7))
print(a.count(8))
#index
a=(1,2,3,4,5,6,7)
print(a.index(7))

#5. Built-in Functions for Tuples
print(len(a))
print(max(a))
print(min(a))
print(sum(a))

#6. Immutability and Tuple Behavior
a=(7, [3,8])
a[1][0]=1000
print(a)