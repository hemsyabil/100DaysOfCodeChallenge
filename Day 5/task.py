# Loops 
for i in range(1, 11):
    print(i)

# List comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)


# For loop
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# do while loop
i = 0
while True:
    print(i)
    i += 1
    if i == 5:
        break

# Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")
