from tkinter import *
window = Tk()
window.title("Hangman game")

window.geometry("{0}x{1}+0+0".format(
    window.winfo_screenwidth(), window.winfo_screenheight()))

def toggle_fullscreen(event):
    window.geometry("500x500+500+200")

window.bind("<Escape>", toggle_fullscreen)

window.mainloop()
