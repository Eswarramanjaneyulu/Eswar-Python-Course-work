#FOR LOOP
'''
a=list(map(int,input("Enter a numbers: ").split()))
current_streak =0
longest_streak =0

for day in a:
    if day ==1:
        current_streak += 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak=0
print("Longest workout streak: ",longest_streak)
'''
