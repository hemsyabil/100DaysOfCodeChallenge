# If Else condition
print("Welcome to the rollercoaster ride")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to ride the rollercoaster.")
else:
    print("You are not eligible to ride the rollercoaster.")

# Modulo operator
print(10 % 3)

# Ternary operator
result = "Eligible" if age >= 18 else "Not eligible"
print(result)

# Looping
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# List comprehension
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

# While loop    
count = 0
while count < 5:
    print(count)
    count += 1

# Function
def greet(name):
    print(f"Hello, {name}!")

greet("John")

# Recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

# Exception handling
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Lambda function
multiply = lambda x, y: x * y
print(multiply(5, 3))

# Dictionary
person = {
    "name": "John Doe",
    "age": 30,
    "is_student": True
}
print(person["name"])

# Dictionary methods
person["city"] = "New York"
print(person)
del person["age"]
print(person)

# Logical operations
print(True and True)
print(True and False)
print(True or False)
print(False or False)
print(not True)
