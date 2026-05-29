import random

# ==============================
#       HANGMAN GAME
# ==============================

# List of predefined words
words = ["apple", "mango", "grapes", "banana", "peach"]

# Randomly select a word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("\n===================================")
print("      WELCOME TO HANGMAN GAME")
print("===================================\n")

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display hidden word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord :", display_word)

    # Check winning condition
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word correctly.")
        break

    # Take user input
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only ONE alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed this letter.")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Correct guess
    if guess in secret_word:
        print("✅ Correct Guess!")

    # Wrong guess
    else:
        wrong_guesses += 1
        remaining = max_wrong_guesses - wrong_guesses

        print("❌ Wrong Guess!")
        print("Remaining Chances :", remaining)

# Losing condition
if wrong_guesses == max_wrong_guesses:
    print("\n===================================")
    print("           GAME OVER")
    print("===================================")
    print("The correct word was :", secret_word)

print("\nThank you for playing Hangman Game!")