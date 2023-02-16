import random

# List of words for the game
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]

# Select a random word from the list
word = random.choice(words)

# Create a list to keep track of the player's guesses
guesses = []

# Set the number of incorrect guesses allowed
max_incorrect_guesses = 6

# Loop through the game until the player wins or loses
while True:
    # Print the current state of the word with underscores for unguessed letters
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)

    # Check if the player has guessed all the letters
    if "_" not in display_word:
        print("You win!")
        break

    # Get the player's guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid guess. Please enter a single letter.")
        continue
    if guess in guesses:
        print("You already guessed that letter. Try again.")
        continue

    # Add the guess to the list of guesses
    guesses.append(guess)

    # Check if the guess is correct
    if guess in word:
        print("Correct!")
    else:
        print("Incorrect.")
        # Increment the number of incorrect guesses
        max_incorrect_guesses -= 1
        # Check if the player has used up all their guesses
        if max_incorrect_guesses == 0:
            print("You lose!")
            break