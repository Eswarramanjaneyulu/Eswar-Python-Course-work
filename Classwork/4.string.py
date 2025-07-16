a="Hello"
b="World!"
c='''This is a multi-line string example.'''

print(a)
print(b)
print(c)

#Operations on Strings
#Concatenation
str1 = "Eswar"
str2 = "Ramanjaneyulu"
str3 = "Chodisetti"
result = str1 + " "+ str2+ " " + str3
print(result)

# Repetition
a="python!"
print(a *7)

a="Eswar Ramanjaneyulu Chodisetti"
print(a[7])     # Indexing
print(a[-7])    # Indexing

print(a[0:7])   # Slicing
print(a[:7])    # Slicing
print(a[7:])    # Slicing

a = "Eswar Ramanjaneyulu Chodisetti"
print("Eswar" in a)      # Membership
print("Ram" not in a)    # Membership
print("satya" not in a)  # Membership

#Built-in String Functions
# 1. len()
a = "Eswar Ramanjaneyulu Chodisetti"
print(len(a))

# 2. max() and min()
a = "EswarRamanjaneyuluChodisetti"
print(max(a))
print(min(a))

# 3. sorted()
a="eswar"
print(sorted(a))

# 4. chr() and ord()
a="A"
b = 77
c="a"
d=108
print(ord(a))
print(chr(b))
print(ord(c))
print(chr(d))

#1. Case Conversion Methods
a="Eswar ramanjaneyulu"
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())
print(a.casefold())

#2. Alignment & Formatting Methods
a="Eswar"
print(a.center(10,"*"))
print(a.ljust(5,"_"))
print(a.rjust(5,"_"))
print(a.zfill(10))

#format()
a="Name:{}, Age:{}"
print(a.format("Eswar",21))

#format_map(mapping)
a="{name} is {age}"
print(a.format_map({'name':'Eswar','age':21}))

#3. Search & Find Methods
a="Banana"
print(a.find("a"))
print(a.rfind("a"))
print(a.index("n"))

#4. String Testing Methods (Boolean Results)
a="Eswar"
print(a.startswith("E")) #true
print(a.endswith("r"))   #true
print(a.isalpha())       #true
print(a.isalnum())       #true
print(a.islower())       #false
print(a.isupper())       #false
print(a.isspace())       #false
print(a.istitle())       #true
print(a.isidentifier())  #true

a="Eswar143"
print(a.isalnum())      #true
a="eswar"
print(a.islower())      #true
a="ESWAR"
print(a.isupper())      #true
a=" "
print(a.isspace())      #true

#5. Replace & Modify Methods
a="eswar"
print(a.replace("eswar","ram"))
print(a.translate("str".maketrans("e","E")))
print(a.maketrans("abc","*@7"))

#6. Splitting & Joining Methods
a="a,b,c,d"
print(a.split(","))
print(a.rsplit(",",1))
a="hello\nworld"
print(a.splitlines())
print(" ".join(["hello","world!"]))
print(a.partition("\n"))
print(a.rpartition("\n"))

#7. Whitespace & Trimming Methods
a = " dhoni "
print(a.strip())
a = "***dhoni"
print(a.lstrip("*"))
a="dhoni&&&"
print(a.rstrip("&"))

#8. Encoding & Decoding Methods
a="Dhoni"
print(a.encode("utf-8"))
a=b"Dhoni"
print(a.decode("utf-8"))

#slicing
a="pythonprogramming"
print(a[6:])
print(a[:6])
print(a[6:12])
print(a[-5:])
print(a[:-5])