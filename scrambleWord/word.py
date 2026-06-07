from tkinter import *
import random

# List of words
words = ["python", "computer", "gaming", "school", "developer"]

# Pick a word and scramble it
word = random.choice(words)
letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters)

# Function to check answer
def check_word():
    guess = entry.get().lower()

    if guess == word:
        result_label.config(text="🎉 Correct!")
    else:
        result_label.config(text=f"❌ Wrong! The word was {word}")

# Create window
window = Tk()
window.title("Word Scramble Game")
window.geometry("400x250")

# Labels
title_label = Label(window, text="🎮 Word Scramble Game", font=("Arial", 16))
title_label.pack(pady=10)

word_label = Label(window, text=scrambled_word, font=("Arial", 20))
word_label.pack(pady=10)

# Entry box
entry = Entry(window, font=("Arial", 14))
entry.pack(pady=10)

# Button
check_button = Button(window, text="Check Answer", command=check_word)
check_button.pack(pady=10)

# Result label
result_label = Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()