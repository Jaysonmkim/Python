weight = float(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in metres:"))
bmi = weight / (height**2)
print(bmi)
if bmi <18.5:
    print("Underweight")
elif 18.5 <=bmi <25:
    print("Normal")
elif 25<= bmi <29.9:
    print("Overweight")
else:
    print("Obese")



