print("Hello World!")


#Type Conversion (Type Casting)
#1. Converting from int
a = 2 
print(float(a)) #2.0
print(str(a))   #'2'
print(bool(a))  #true
#print(list(int))  #error int is not iterable
#print(set(int))   #error int is not iterable
#print(tuple(int)) #error int is not iterable
#print(dict(int))  #error int is not iterable


#2. Converting from float

a=7.0
print(int(a))      #7
print(str(a))      #'7.0'
print(bool(a))     #true
#print(list(a))    #error float is iterable
#print(set(a))     #error float is iterable
#print(tuple(a))   #error float is iterable
#print(dict(a))    #error float is iterable

#3. Converting from str
print(int('7'))       #'7'
#print(int("eswar"))  #error invlid literal
print(float('7.0'))   #'7.0'
#print(float("eswar")) #error invlid string
#print(dict("eswar"))   #error Needs key-value pair structure

a="dhoni"
print(list(a))
print(set(a))
print(tuple(a))

#4. Converting from list
l=[1,2,3,4,5,6,7]
#print(int(l))    #error not allowed
#print(float(l))  #error not allowed
#print(dict(l))   #error Needs list of key-value pairs
print(str(l))
print(set(l))
print(tuple(l))
print(bool(l))

#5. Converting from tuple 
t=(1,2,3,4,5,6,7)
#print(int(t))    #error not allowed
#print(float(t))  #error not allowed
#print(dict(t))   #error Needs must be tuple of key-value pairs
print(str(t))
print(list(t))
print(set(t))
print(bool(t))
#6. Converting from set
s={1,2,3,4,5,6,7}
#print(int(s))    #error not allowed
#print(float(s))  #error not allowed
#print(dict(s))   #error Needs must be iterable of key-value pairs
print(str(s))
print(list(s))
print(tuple(s))
print(bool(s))

#7. Converting from dict
d={1:7,2:18,3:45,}
#print(int(d))    #error not allowed
#print(float(d))  #error not allowed
print(str(d))
print(list(d))
print(tuple(d))
print(set(d))
print(bool(d))

#8. Converting from bool
b = True
o = False
print(int(b))
print(int(o))
print(float(b))
print(float(o))
print(str(b))
print(str(o))
#print(list(b))     error not iterable
#print(tuple(b))    error not iterable
#print(set(b))      error not iterable
#print(dict(b))     error not iterable

#9. Dictionary Conversion
#To convert a list to a dictionary, it must be a list of key-value tuples.
#tuple-dict
d = (('name', 'teja'), ('batch', '22'), ('subject', 'python'))
print(dict(d))
#list-dict

d = [('name', 'teja'), ('batch', '22'), ('subject', 'python')]
print(dict(d))
#set-dict

d = {('name', 'teja'), ('batch', '22'), ('subject', 'python')}
print(dict(d))