from tkinter import *
import random

# List of words
words = ["python", "computer", "gaming", "school", "developer"]

# Global word variables
word = ""
scrambled_word = ""

# Function to generate a new word
def new_word():
    global word, scrambled_word

    word = random.choice(words)

    letters = list(word)
    random.shuffle(letters)
    scrambled_word = "".join(letters)

    word_label.config(text=scrambled_word)
    entry.delete(0, END)
    result_label.config(text="")

# Function to check answer
def check_word():

    try:
        guess = entry.get().lower()

        if guess == "":
            raise ValueError("Please enter a word")

        if guess == word:
            result_label.config(text="🎉 Correct!")
        else:
            result_label.config(text=f"❌ Wrong! The word was {word}")

    except ValueError as error:
        result_label.config(text=error)

# Create window
window = Tk()
window.title("Word Scramble Game")
window.geometry("400x300")

# Title
title_label = Label(window, text="🎮 Word Scramble Game", font=("Arial", 16))
title_label.pack(pady=10)

# Scrambled word display
word_label = Label(window, text="", font=("Arial", 20))
word_label.pack(pady=10)

# Input box
entry = Entry(window, font=("Arial", 14))
entry.pack(pady=10)

# Buttons
check_button = Button(window, text="Check Answer", command=check_word)
check_button.pack(pady=5)

next_button = Button(window, text="Next Word", command=new_word)
next_button.pack(pady=5)

# Result
result_label = Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start first word
new_word()

window.mainloop()