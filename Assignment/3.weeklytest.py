#1.BMI
'''
def calculate_bmi(weight,height):
    return weight/(height*height)
weight=int(input("Enter a weight: "))
height=float(input("Enter a height: "))
calculate_bmi(weight,height)
print(calculate_bmi(weight,height))

# 2.filter even numbers
def filter_even(numbers):
    even_numbers=[]
    for num in numbers:
        if num%2==0:
            even_numbers.append(num)
    return even_numbers
numbers=eval(input())
result=filter_even(numbers)
print("Even numbers:",result)

# 3.Generate Multiplication table
def generate_table(a):
    for i in range(1,11):
        print(f"{a}x{i}={a*i}")
           
num=int(input("Enter a number: "))
generate_table(num)

# 4.check Anagram
def is_anagram(str1,str2):
    str1 = str1.replace(" ", " ").lower()
    str2 = str2.replace(" ", " ").lower()
    
    return sorted(str1) == sorted(str2)

str1 = input("Enter a first string: ")
str2 = input("Enter a second string: ")

if is_anagram(str1,str2):
    print("True")
else:
    print("Flase")

# 5.Count Word Occurrences
def count_word(text):
    words= text.lower().split()
    word_count={}
    
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word] = 1
    return word_count
sentence=input("Enter a sentence: ")
result = count_word(sentence)
for word,count in result.items():
    print(f"{word}:{count}")

#6.Simulate LUR Cache
def lur_cache(request,size):
'''    