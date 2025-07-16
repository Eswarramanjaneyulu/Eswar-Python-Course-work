# Creating a set with unique elements
my_set = {1, 2, 3, 4}
# Creating an empty set (use set() function, not {})
empty_set = set()
# Set with duplicate elements (duplicates are removed automatically)
set_with_duplicates = {1, 2, 2, 3, 4}
print(set_with_duplicates) # Output: {1, 2, 3, 4}


#2. Set Properties
# This will raise a TypeError
#invalid_set = {[1, 2], 3}
# Lists are mutable and cannot be added to a set

#3. Operations on Sets
#a. Membership Testing
s = {1,2,3,4,5,6,7}
print(3 in s)
print(8 in s)
print(7 not in s)
print(10 not in s)

#b. Union (| or union() method)
s1={1,2,3,4}
s2={4,5,6,7}
print(s1|s2)
#c. Intersection (& or intersection() method)
print(s1&s2)
#d. Difference (- or difference() method)
print(s1-s2)
#e. Symmetric Difference (^ or symmetric_difference() method)
print(s1^s2)
#f. Subset (<= or issubset() method)
print(s1<=s2)
#g. Superset (>= or issuperset() method)
print(s1>=s2)
#h. Disjoint Sets (isdisjoint() method)
print(s1.isdisjoint(s2))

#4. Built-in Methods for Sets
s1={1,2,3,4}
s1.add(5)
print(s1)
s1.remove(5)
print(s1)
s1.discard(4)
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)

s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
s1={7,3,8,9}
s1.update({18})
print(s1)

s1={1,2,3,4,5,6,7}
s2={6,7,8,9,10}
s3={7,8,9,18}
s1.intersection_update(s2,s3)
print(s1)

s1={1,2,3,4,5,6,7}
s2={6,7,8,9,10}
s3={7,8,9,18}
s1.difference_update(s2,s3)
print(s1)

s1={1,2,3,4,5,6,7}
s2={6,7,8,9,10}
s3={7,8,9,18}
s1.symmetric_difference_update(s2)
print(s1)

s1={1,2,3,4,5,6,7}
s2={6,7,8,9,10}
s3={7,8,9,18}
s4=s1.copy()
print(s4)

s1={1,2,3}
s2={8,9,7}
s3={7,8,9,18}
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s3))

s1={1,2,3,4,5,6,7}
s2={6,7,8,9,10}
s3={7,8,9,18}
s4={7,8,9,18}
print(s1.issubset(s2))
print(s3.issubset(s4))

s1={1,2,3,4,5,6,7}
s2={6,7,8,9,10}
s3={7,8,9,18}
s4={7,8,18}
print(s1.issuperset(s2))
print(s3.issuperset(s4))

#built-in function for sets
s1={1,2,3,4,5,6,7}
print(len(s1))
print(max(s1))
print(min(s1))
print(sum(s1))
print(sorted(s1))

s1=[1,2,3,4,7]
print(set(s1))

#immutability and frozensets
s1=frozenset([1,7,2,18])
print(s1)

s1=frozenset([1,7,2,18])
s2=s1.union([45])
print(s2)
