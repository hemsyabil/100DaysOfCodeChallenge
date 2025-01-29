# function with input parameters
def greet_user(name):
    print(f"Hello, {name}!")


# calling the function with an argument
# greet_user("John Doe")


def life_in_weeks(age):
    remaining_weeks = (90-age)*52
    
    print(f"You have {remaining_weeks} weeks left.")
    
age = 36
life_in_weeks(age)

# keyword arguments
def greet_user_with_age(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# greet_user_with_age(age=36, name="John Doe")

# default arguments
def greet_user_with_default_age(name, age=30):
    print(f"Hello, {name}! You are {age} years old.")

# greet_user_with_default_age("John Doe")

def calculate_love_score(name1, name2):
    # Combine both names for easier processing
    combined_name = (name1 + name2).lower()
    
    # Count occurrences of the letters in "TRUE" and "LOVE"
    count_true = sum(combined_name.count(char) for char in "true")
    count_love = sum(combined_name.count(char) for char in "love")
    
    # Calculate and print the love score
    print(f"True Love Sore: {count_true}{count_love}")

    
name1 = "Bharat Kumar Regmi" #
name2 = "Deepa Tiwari"
calculate_love_score(name1, name2)