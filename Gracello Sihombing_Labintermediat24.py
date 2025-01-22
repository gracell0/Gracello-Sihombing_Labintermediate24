secret_word = "gracello"

def hangman():
    word = "gracello"
    revealed = ""
    index = 0

    print("Welcome to hangman")

    while index < len(secret_word):
        print("\nWord:", revealed + "_" * (len(secret_word) - index))

        guess = input(f"Guess the next letter ({index + 1}/{len(secret_word)}): ").lower()

        if len(guess) != 1 or not guess.isalpha():
          print("Please enter a single valid letter.")
          continue

        if guess == secret_word[index]:
           revealed += guess
           index += 1
        else:
           print("Wrong guess! Try again.")
        
        
    print(f"\nCongratulations! You guessed the word: {secret_word}")
    
hangman()