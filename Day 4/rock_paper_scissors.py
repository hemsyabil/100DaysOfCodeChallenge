import random

rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
'''

paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
'''

scissors = '''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/                                   
'''

print("Welcome to rock paper scissors game!")


def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Enter your choice (rock, paper, scissors): ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "\nIt's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "\nYou win!"
    else:
        return "\nComputer wins!"
    

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {rock if user_choice == 'rock' else (paper if user_choice == 'paper' else scissors)}\nComputer chose: {rock if computer_choice == 'rock' else (paper if computer_choice == 'paper' else scissors)}")
    print(determine_winner(user_choice, computer_choice))

    play_again = input("Do you want to play again? (yes/no): ").lower()
    while play_again != 'yes' and play_again != 'no':
        play_again = input("Invalid choice. Do you want to play again? (yes/no): ").lower()

    if play_again == 'yes':
        play_game()

play_game()
