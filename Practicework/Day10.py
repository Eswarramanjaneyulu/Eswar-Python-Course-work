#function
#even or odd
def even_or_odd(a):
    if a%2==0:
        return "Even"
    else:
        return "Odd"
a=int(input())
print(even_or_odd(a))

#squares of numbers
def squares(a):
    return a*a
a=int(input())
print(squares(a))

# division of two num
def div(a,b):
    return a/b
a=int(input())
b=int(input())
print(div(a,b))

#even or odd by use lambda
a=int(input())
iseven=lambda a: "Even" if a%2==0 else "Odd"
print(iseven(a))

#squares of numbers by use lambda
a=int(input())
b=lambda a:a*a
print(b(a))

#division of two num by use lambda
a=int(input())
b=int(input())
div=lambda a,b:a/b
print(div(a,b))
