import random

def choose_word():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    return random.choice(word_list) # Select a random word from the list

# Function to display the current state of the word with blanks and guessed letters
def display_word(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    return display

def play_hangman():
    selected_word = choose_word()
    guessed_letters = [] # Create a list to track guessed letters
    max_attempts = 6 # Maximum number of allowed incorrect guesses before losing
    attempts = 0

    while attempts < max_attempts:
        print("Word: " + display_word(selected_word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in selected_word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts += 1

        if set(guessed_letters) == set(selected_word):
            print("Congratulations! You've guessed the word: " + selected_word)
            break

    if attempts == max_attempts:
        print("You've run out of attempts. The word was: " + selected_word)

while True:
    play_hangman()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
