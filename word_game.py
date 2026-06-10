import random

# List of words
words = ["python", "computer", "gaming", "school", "developer"]

def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)

def play_game():
    score = 0

    print("\n🎮 WORD SCRAMBLE GAME (CONSOLE VERSION)")
    print("Type 'exit' to quit\n")

    while True:
        word = random.choice(words)
        scrambled = scramble_word(word)

        print(f"Scrambled word: {scrambled}")

        guess = input("Your answer: ").lower()

        # Exit condition
        if guess == "exit":
            print("\n👋 Game Over!")
            print(f"Final Score: {score}")
            break

        # Empty input check
        if guess.strip() == "":
            print("❌ Please enter a word!\n")
            continue

        # Check answer
        if guess == word:
            print("🎉 Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The word was: {word}\n")

# Run game
play_game()