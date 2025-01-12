print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = input("How much tip would you like to give? 10, 12 or 15? ")
number_of_splits = int(input("How many people to splits the bill? "))

tip_amount = int(tip_percentage)/100

amount_per_person = (total_bill + (total_bill * tip_amount))/number_of_splits
print(f"Each person should pay: ${amount_per_person}")