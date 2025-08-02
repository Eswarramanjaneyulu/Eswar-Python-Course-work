#1.BMI
def calculate_bmi(weight,height):
    return weight/(height*height)
weight=int(input())
height=float(input())
calculate_bmi(weight,height)
print(calculate_bmi(weight,height))
