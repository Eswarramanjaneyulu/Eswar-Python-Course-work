a=7
b=7.0
c=7j
print(type(a))
print(type(b))
print(type(c))

#Sequence Types
a="eswar"
b=["eswar","mani","aditya"]
c=("eswar","mani","aditya")
print(type(a))
print(type(b))
print(type(c))
b.append("venky")
print(b)
b.append(["E0","C2","B9","F0"])
print(b)

#set type
a={"eswar","mani","aditya"}
b=frozenset(["eswar","mani","aditya"])
print(type(a))
print(type(b))
a.add("venky")
a.add("sai")
print(a)

#mapping type
a={"name":"eswar","age":21, "gender":"male","phno":9014584004}
print(type(a))
print(a)
a["rating"]="5star"
print(a)

#boolean type
a=7
b=7
print(a<b)
print(a>b)
print(a==b)
