#Sets
#a={1,2,3,4,5,6,7}

a={1,2,3,4,5,5,6,6,7,7}   #it's a set so, no duplicates values
print(a)


#Operations on Sets
#a. Membership Testing
a={1,2,3,4,5,6,7}
print(3 in a)
print(3 not in a)
print(8 in a)
print(8 not in a)


#b. Union (| or union() method)
a={1,2,3,4,5,6,7}
b={7,8,9,10}   
c={7,45,33}
# tow set are combine elements
print(a|b)
#Intersection (& or intersection() method)
print(a&b)           # common element in both sets
print(a&b&c)         # common element in all  sets
#Difference (- or difference() method)
print(a-b)

# Symmetric Difference (^ or symmetric_difference() method)

a={1,2,3,4,5,6,7}
b={7,8,9,10}         # common element will be not print and reamin two set are print
print(a^b)
#f. Subset (<= or issubset() method)  
a={7,8,9,10}
b={7,8,9,10,18}    # a all set elements  in b set elements  it's subset   
print(a<=b)
#g. Superset (>= or issuperset() method)
print(a>=b)       # b all set elements  in a set elements  it's superset
#h. Disjoint Sets (isdisjoint() method)
a = {1, 2, 3}
b = {4, 5, 6}     # both set are different it's a isdisjoint
print(a.isdisjoint(b))

#Built-in Methods for Sets
a={1,2,3,4,5,6,7}
a.add(18)
print(a)
a.remove(18)
print(a)
a.discard(5)
print(a)
a.pop()
print(a)
a.clear()
print(a)

#Built-in Functions for Sets
a={1,2,3,4,7,6,5}
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sorted(a))
print(set([1,2,3,7]))

#6. Immutability and Frozensets
a=frozenset([1,2,3,7])
print(a)       # it's immutables conn't be change
