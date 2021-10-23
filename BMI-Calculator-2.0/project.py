height = float(input("enter a your height in m: "))
weight = float(input("enter a your weight in kg: "))

bmi    = round(weight/height ** 2)
if bmi < 18.5:
    print("They are under weight")
    
elif bmi > 18.5:
    print("They are normal weight")

elif bmi < 25:
    print("They are over weight")
elif bmi < 30:
    print("They are obese")
    
else:
    print("They are clinicaly obese")        
