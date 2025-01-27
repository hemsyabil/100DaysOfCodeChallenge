import random
from hangman_art import hangman, hangman_stages
from hangman_words import words


random_word = random.choice(words)

print('Welcome to Hangman!')
print(hangman)

word_length = len(random_word)
placeholder = ''
lives = 0

for i in range(word_length):
    placeholder += '_'

print(f"Word to guess: {placeholder}")

game_over = False
guessed_letters = []

while not game_over:
    print(f"********************* ({lives}/6 lives left) *********************")
    guess = input('Guess the letter: ').lower()

    if guess in guessed_letters:
        print(f"You have already guessed {guess}")

    display = ''
        
    for letter in random_word:
        if letter == guess:
            display += letter
            guessed_letters.append(guess)
        elif letter in guessed_letters:
            display += letter
        else:
            display += '_'

    if guess not in random_word:
        lives += 1

        print(f"You guessed {guess}; that's not in the word. You lose a life.")
        if lives == 6:
            game_over = True
            print(f"********************* It was {random_word}! You Lose. *********************")

    print(f"Word to guess: {display}")

    if "_" not in display:
        game_over = True
        print("********************* Congratulation! You Won!. *********************")

    print(hangman_stages[lives])
