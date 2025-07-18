# Tuple
'''
a=1,2,3
print(type(a))

a=(1,2,3,4,5,6,7)
print(a[2])
print(a[-2])
print(a[1:6])
print(a[:4])
print(a[2:])
b=(18,45,33,8,17)
print(a+b)
print(a *2)
print(2 in a)
print(18 in a)
print(8 not in a)
print(3 not in a)
a=(18,7,7)
x,y,z =a
print(x,y,z)
print(a.count(7))
print(a.index(7))
print(len(a))
print(max(a))
print(min(a))
print(sum(a))

a=(1,[7,18,8,9,6,5])
a[1][5]=10
print(a)

#Dictionary
student={
    "name": "Eswar",
    "age": 21,
    "course": "python"
}
print(student)
print(student["name"])
print(student["age"])
print(student.get("name"))
print(student.get("age"))
#print(student("city"))
print(student.get("city"))   #we use get it  will be none other wise it show key type error  
student["city"]="kajuluru"   #adding and updating iteam
print(student)
city = student.pop("city")   # remove a element by using pop 
print(city)
print(student)
del student["age"]
print(student)

student={
    "name": "Eswar",
    "age": 21,
    "course": "python",
    "city": "kajuluru"
}
student.popitem()
print(student)
student.clear()
print(student)


student={
    "name": "Eswar",
    "age": 21,
    "course": "python",
    "city": "kajuluru"
}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("course"))
print(student.get("street"))
print(student)
print(student.setdefault("state"))
student.update({"gander":"male"})
print(student)
print(len(student))
print(max(student))
print(min(student))
print(sorted(student))

#Nested Dictionaries
student = {
    "Eswar": {"age":21,"course":"python"},
    "mani":{"age":20,"course":"data science"}
}
print(student["Eswar"]["course"])
print(student["Eswar"]["age"])
print(student["mani"]["course"])
print(student["mani"]["age"])

#Dictionary Comprehension
for x in range(1,6):
    squares={x:x*x}
    print(squares)

#Real-Time Problems Using Dictionaries
#Problem 1: Count the Frequency of Words in a Sentence
s="hello world hello python"
word_count={}

for word in s.split():
    word_count[word]=word_count.get(word, 0)+1
print(word_count)

#Problem 2: Find the Student with the Highest Marks
student ={
    "eswar":85,
    "mani":90,
    "aditya":88
}
top_student = max(student, key=student.get)
print(top_student)
'''

#Sets
a={1,2,3,4,5,6,7}
#Operations on sets
