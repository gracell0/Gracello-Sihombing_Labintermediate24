def updateText(secret_word, guessed_letters):
    display_word = "".join(letter if letter in guessed_letters else "_" for letter in secret_word)
    return display_word

def hangman(secret_word):
    guessed_letters = set()
    attempts = 6  # Maximum allowed attempts

    print("Welcome to Hangman!")
    
    while attempts > 0:
        display_word = updateText(secret_word, guessed_letters)
        print("\nWord:", display_word)
        print(f"Attempts left: {attempts}")

        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the secret word!")
        else:
            print(f"Wrong guess! '{guess}' is not in the secret word.")
            attempts -= 1

    print(f"\nGame over! The word was: {secret_word}")

hangman("indonesia") # Start the game