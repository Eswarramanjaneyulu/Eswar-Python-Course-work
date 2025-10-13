'''
# Generators
def my_generation():
    yield 1
    yield 2
    yield 3
    yield 4
gen=my_generation()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def square(a):
    for i in range(1,a+1):
        yield i*i
for num in square(5):
    print(num)

gen=(x*x for x in range(5))
print(list(gen))        

gen =(x*x for x in range(5))
print(next(gen)) 
print(next(gen)) 
print(list(gen))

def simple_generation():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("End")
gen=simple_generation()
print(next(gen))
print(next(gen))
print(next(gen))

def square(a):
    for i in range(a):
        yield i*i
a=square(5)
print(next(a))
print(next(a))
print(list(a))

def count_up_to(a):
    count=1
    while count<=a:
        yield count
        count+=1
x=count_up_to(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

def count_down(a):
    while a>0:
        yield a
        a-=1
cd=count_down(3)
print(next(cd))
print(next(cd))
print(next(cd))

def strem_vide(a):
    for i in a:
        yield i
video=[1,2,3,4]
player=strem_vide(video)
print(next(player))

from datetime import date
today = date.today()
print("Today's date:", today)

s=input()
m=s[6:]+s[2:6]+s[:2]
a=m.replace("-","/")
print(a)

a=input()
b={}
for char in a:
    if char !=' ':
        if char in b:
            b[char]+= 1
        else:
            b[char]=1
print(b) 

from datetime import date
today = date.today()
print("Today's date:",today)
specific_date=date(2003, 9, 12)
print("Specific date:",specific_date)
print("Year:",today.year)
print("Month:",today.month)
print("Day:",today.day)

from datetime import datetime
specific_date_time=datetime.now()
print("Specific time:",specific_date_time)

from datetime import datetime
now=datetime.now()
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

from datetime import date
today = date.today()
print("Weekday (0=Monday, 6=Sunday):", today.weekday())
print("ISO Weekday (1=Monday, 7=Sunday):", today.isoweekday())

from datetime import time
specific_time = time(7,7,7)
print("Specific time:", specific_time)

from datetime import time
specifi_time=time(7,7,7)
print("Hour:",specifi_time.hour)
print("Minute:",specifi_time.minute)
print("Second:",specifi_time.second)

from datetime import datetime
Time=datetime.now()
print("Current date and time:",Time)

from datetime import datetime
Time=datetime(2025,10,10,12,0,1)
print("specifi date and time:",Time)

from datetime import datetime
Time=datetime.now()
print("Year:",Time.year)
print("Month:",Time.month)
print("Day:",Time.day)
print("Hour:",Time.hour)
print("Minute:",Time.minute)
print("Second:",Time.second)

from datetime import datetime
formatted_date = datetime.now().strftime("%Y-%m-%d")
formatted_time = datetime.now().strftime("%H:%M:%S")
formatted_datetime = datetime.now().strftime("%d-%b-%Y %I:%M %p")
print("Formatted Date:", formatted_date)
print("Formatted Time:", formatted_time)
print("Formatted Date and Time:", formatted_datetime)

from datetime import datetime
now=datetime.today()
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M:%S")
formatted_datetime = now.strftime("%d-%b-%Y %I:%M %p")
print("Formatted Date:", formatted_date)
print("Formatted Time:", formatted_time)
print("Formatted Date and Time:", formatted_datetime)

from datetime import datetime
date_string = "16-02-2024 14:30"
parsed_date = datetime.strptime(date_string, "%d-%m-%Y %H:%M")
print("Parsed Date and Time:", parsed_date)

from datetime import date, timedelta
today = date.today()
future_date = today + timedelta(days=7)
print("Date after 7 days:", future_date)
past_date = today - timedelta(days=3)
print("Date 3 days ago:", past_date)
'''
from datetime import datetime, timedelta
now = datetime.today()
future_time = now + timedelta(hours=2)
print("Time after 2 hours:", future_time)