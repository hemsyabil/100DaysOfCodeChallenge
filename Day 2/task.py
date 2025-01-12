# String subscription
print("Hello, World!"[0:5])

# String concatenation
greeting = "Hello, "
name = "John"
print(greeting + name)

# String formatting
age = 30
print(f"My name is {name} and I am {age} years old.")

# String methods
sentence = "This is a sentence."
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.replace("sentence", "paragraph"))
print(sentence.count("is"))

# Integer
number = 10
print(number + 5)
print(number - 5)
print(number * 5)
print(number / 5)
print(number % 5)

# large integers
large_number = 123_345_678
print(large_number)

# Float
decimal_number = 10.5
print(decimal_number + 5)
print(decimal_number - 5)
print(decimal_number * 5)
print(decimal_number / 5)
print(decimal_number ** 2)

# Boolean
true_value = True
false_value = False
print(true_value and false_value)
print(true_value or false_value)
print(not true_value)

# List
numbers = [1, 2, 3, 4, 5]
print(numbers[0])
print(numbers[1:3])
numbers.append(6)
print(numbers)
numbers.remove(3)

# Dictionary
person = {
    "name": "John Doe",
    "age": 30,
    "is_student": True
}
print(person["name"])

# dictionary methods
person["city"] = "New York"
print(person)
del person["age"]
print(person)

# Set
numbers_set = {1, 2, 3, 3, 4, 4, 5}
print(numbers_set)

# Tuple
coordinates = (10, 20)
print(coordinates[0])

# Data type checking
print(isinstance(numbers, list))
print(isinstance(coordinates, tuple))
print(isinstance(numbers_set, set))
print(isinstance(person, dict))
print(isinstance(greeting, str))
print(isinstance(age, int))

# Type conversion
print(float(age))
print(int(decimal_number))
print(str(coordinates))

# Error handling
try:
    print(numbers[6])
except IndexError:
    print("Index out of range.")

name_len = len(input("Enter your name: "))
print("Number of letters in your name: " + str(name_len))
print(f"Number of letters in your name: {name_len}")


# Assignment operations
number = 10
number += 5
print(number)
number -= 5
print(number)
number *= 5

# List comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)