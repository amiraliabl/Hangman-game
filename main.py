from tkinter import *
from tkinter import ttk

def toggle_fullscreen(event):
    window.geometry("500x500+500+200")

def start_game():
    selected_category = category_var.get()
    print(f"Starting game with category: {selected_category}")
    # Add code here to initialize the game with the selected category

# Initialize the main window
window = Tk()
window.title("Hangman Game")
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.configure(bg="#f0f0f0")
window.bind("<Escape>", toggle_fullscreen)

# Create and configure the main frame
main_frame = Frame(window, bg="#ffffff", bd=10, relief=RIDGE)
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Title label
title_label = Label(main_frame, text="Welcome to Hangman!", font=("Helvetica", 24, "bold"), bg="#ffffff")
title_label.grid(column=0, row=0, pady=20)

# Category selection
category_label = Label(main_frame, text="Select Category:", font=("Helvetica", 14), bg="#ffffff")
category_label.grid(column=0, row=1, pady=10)

category_var = StringVar(value="Animals")
categories = ["Animals", "Fruits", "Countries", "Movies", "Sports"]

category_menu = ttk.Combobox(main_frame, textvariable=category_var, values=categories, font=("Helvetica", 14))
category_menu.grid(column=0, row=2, pady=10)

# Start button
start_button = Button(main_frame, text="Start Game", font=("Helvetica", 14), command=start_game)
start_button.grid(column=0, row=3, pady=20)

window.mainloop()