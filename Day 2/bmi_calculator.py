weight_in_kg = input("Enter your weight in kg: ")
height_in_cm = input("Enter your height in cm: ")

# BMI = weight_in_kg / height_in_meter (squared)
height_in_meter = float(height_in_cm) / 100
bmi = float(weight_in_kg) / (height_in_meter ** 2)

print("Your BMI is:", round(bmi))

# BMI categories    
if bmi < 18.5:
    print("You are Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("You are in Normal weight")
elif bmi >= 25 and bmi < 30:
    print("You are Overweight")
