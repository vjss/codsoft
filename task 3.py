import tkinter as tk
import random

def play():
    player_choice = player_choice_var.get()
    computer_choice = random.choice(choices)
    
    result = determine_winner(player_choice, computer_choice)
    
    result_label.config(text=f"Computer chose {computer_choice}. {result}")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Create the main application window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Available choices
choices = ["Rock", "Paper", "Scissors"]

# Player choice
player_choice_var = tk.StringVar()
player_choice_var.set("Rock")

# Label for player choice
player_label = tk.Label(root, text="Your choice:")
player_label.grid(row=0, column=0)

# Dropdown menu for player choice
player_dropdown = tk.OptionMenu(root, player_choice_var, *choices)
player_dropdown.grid(row=0, column=1)

# Button to play
play_button = tk.Button(root, text="Play", command=play)
play_button.grid(row=1, columnspan=2)

# Label for displaying result
result_label = tk.Label(root, text="")
result_label.grid(row=2, columnspan=2)

# Run the Tkinter event loop
root.mainloop()