from tkinter import *
import random

# Create window
window = Tk()
window.title("Choose a Door")
window.geometry("400x300")

# Randomly choose what's behind each door
doors = ["💰 Treasure", "💀 Trap", "📦 Empty Room"]
random.shuffle(doors)

# Function for door choice
def choose_door(number):
    result_label.config(text=f"Door {number}: {doors[number - 1]}")

# Title
title_label = Label(window, text="🚪 Choose a Door", font=("Arial", 16))
title_label.pack(pady=20)

# Door buttons
door1 = Button(window, text="Door 1", width=10,
               command=lambda: choose_door(1))
door1.pack(pady=5)

door2 = Button(window, text="Door 2", width=10,
               command=lambda: choose_door(2))
door2.pack(pady=5)

door3 = Button(window, text="Door 3", width=10,
               command=lambda: choose_door(3))
door3.pack(pady=5)

# Result
result_label = Label(window, text="", font=("Arial", 14))
result_label.pack(pady=20)

window.mainloop()