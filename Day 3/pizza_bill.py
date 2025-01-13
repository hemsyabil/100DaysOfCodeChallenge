print("Welcome to pizza ordering")

# variables
large_size = 25
medium_size = 20
small_size = 15

pepperoni_cost = 3
extra_cheese = 1
total_cost = 0

size = input("What size would you like (S, M, L)? ")
is_pepperoni = input("Do you want to add pepperoni? (yes/no)")
is_cheese = input("Do you want to add extra cheese? (yes/no)")

# calculate cost
if size == "S":
    total_cost += small_size
elif size == "M":
    total_cost += medium_size
else:
    total_cost += large_size


if is_pepperoni.lower() == "yes":
    total_cost += pepperoni_cost

if is_cheese.lower() == "yes":
    total_cost += extra_cheese
    
print(f"Your total cost is ${total_cost}")
