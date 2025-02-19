import random

wins, losses = 0, 0
word_list = ["one", "two", "three", "four", "five"]

def play_hangman(word):
    """Plays one round of Hangman."""
    global wins, losses
    guessed, attempts = set(), 6

    while attempts > 0:
        display = "".join(c if c in guessed else "_" for c in word)
        print(f"\nWord: {display} | Attempts left: {attempts}")

        if "_" not in display:
            print(f"🎉 You won! The word was '{word}'")
            wins += 1
            return

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha() or guess in guessed:
            print("⚠️ Invalid guess. Try again.")
            continue

        guessed.add(guess)
        if guess not in word:
            attempts -= 1

    print(f"💀 You lost! The word was '{word}'")
    losses += 1

def start_game():
    """Runs the Hangman game loop."""
    global word_list

    while word_list:
        play_hangman(word_list.pop(random.randint(0, len(word_list) - 1)))
        print(f"\n🏆 Wins: {wins} | ❌ Losses: {losses}")
        if input("Play again? (yes/no): ").strip().lower() != "yes":
            break

    print(f"\nGame Over! 🏆 Wins: {wins} | ❌ Losses: {losses}")

# Start the game
start_game()