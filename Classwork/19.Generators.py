#Example
'''
def simple_generator():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("End")
gen=simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))
'''
def count_up_to(a):
    count=1
    while count<=a:
        yield count
        count+=1
n=int(input())
counter=count_up_to(n)
print(next(counter))
print(next(counter))
















