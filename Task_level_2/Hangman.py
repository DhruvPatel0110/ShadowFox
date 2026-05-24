# Simple Hangman Game
import random

# List of words
words = ["python", "shadowfox", "internship", "developer", "hangman"]

# Choosing a random word
secret_word = random.choice(words)

guessed_word = ["_"] * len(secret_word)
guessed_letters = []
attempts = 6
print("Welcome to Hangman Game")

# Game loop
while attempts > 0 and "_" in guessed_word:

    print("\nWord :", " ".join(guessed_word))

    guess = input("Enter a letter : ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter")
        continue
    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct Guess")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("Wrong Guess")
        print(f"Attempts Left : {attempts}")

# Win condition
if "_" not in guessed_word:
    print("\nCongratulations! You Won")
    print("The word was :", secret_word)

# Loss condition
else:
    print("\nGame Over")
    print("The word was :", secret_word)