# Random number generator
import random
import my_module


def generate_random_number():
    return random.randint(1, 100)


# User input
user_number = int(input("Enter a number between 1 and 100: "))

# Generate random number
random_number = generate_random_number()

# Check if the user guessed correctly
if user_number == random_number:
    print("Congratulations! You guessed the correct number.")
else:
    print(f"Sorry, the correct number was {random_number}.")

# Check if the user's guess was higher or lower than the random number
if user_number > random_number:
    print("Your guess was higher than the random number.")
else:
    print("Your guess was lower than the random number.")

print(my_module.my_favorite_number)

# Heads or tail generator
coin_flip = random.choice(["Heads", "Tails"])
print(f"The coin landed on {coin_flip}.")

# Fibonacci sequence generator
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


print(fibonacci(10))

# Palindrome checker
def is_palindrome(string):
    return string == string[::-1]


# user_string = input("Enter a string: ")
# print(is_palindrome(user_string))

# Lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(random.choice(states_of_america))

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
