import random
import time
import msvcrt
import os

# function for scrambling the word

def generate_scrambled_word(word1):
    word_list = list(word1)
    scrambled = ""

    for i in range(0, len(word1)):
        index = random.randint(0, len(word_list) - 1)
        scrambled += word_list.pop(index)  # Remove and append a random letter

    return scrambled

def main_game():
    initial_word = random.choice(word_bank)
    scrambled_word = generate_scrambled_word(initial_word)
    print(scrambled_word, "\n")

    attempts_remaining = max_attempts

    while attempts_remaining > 0:
        inputword = input(f"Enter your guess, {attempts_remaining} attempts left: ")
        if inputword.lower() == initial_word.lower():
            print("Congrats! You guessed it.")
            break
        else:
            attempts_remaining -= 1
            print(f"That is not the right word. Try again. {attempts_remaining} attempts remain.\n")
            continue

    if attempts_remaining == 0:
        print(f"The correct word was {initial_word}.")

# ^^main function

max_attempts = 5
word_bank = ["zebra", "dog", "elephant", "mammoth",
             "cheetah", "mouse", "chicken", "goose"]

print("Welcome to the word-o-mator...\n")
time.sleep(3)
print("A word at random will be generated\n")
time.sleep(1)
print(f"You must guess the word within {max_attempts} attempts\n")
time.sleep(1)

while True:
    main_game()

    print("Would you like to play again? Press Y for yes and N for no.\n")

    while True:
        key = msvcrt.getch().decode("utf-8").lower()

        if key == 'y':
            time.sleep(1)
            os.system('cls')
            break
        elif key == 'n':
            print("Thanks for playing.\n")
            quit()
        else:
            print("Invalid key. Please try again.\n")
