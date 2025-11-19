'''
#practice
nums=[2,7,4,5,1,3]
target=6
seen =set()
res=[]
for n in nums:
    if target - n in seen:
        res.append((target - n,n))
    seen.add(n) 
print(res)

l = list(map(int, input().split()))
maximum = max(l)

for i in range(min(l), maximum + 1):
    if i not in l:
        print(i)
        break
else:
    print(maximum + 1)

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))

if len(l1)>len(l2):
    l1,l2=l2,l1
    
for i in l1:
    if i in l2:
        print(i)
print(set(l1)& set(l2))

s=input("Enter a string: ")
vol_cnt=0
con_cnt=0
word_cnt=0

vol="aeiouAEIOU"

for i in s:
    if i in vol:
        vol_cnt+=1
    elif i.isalpha() and i not in vol:
        con_cnt+=1
    elif i.isspace():
        word_cnt+=1
print(f"vol: {vol_cnt}\ncon:{con_cnt}\nwords:{word_cnt}")
'''
