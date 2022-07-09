from tkinter import *
from tkinter import font

root = Tk()
root.title('Empire Editor')
root.geometry("500x500")

our_font = font.Font(family="Empires Alphabet", size=32)

my_frame = Frame(root, width=480, height=275)
my_frame.pack(pady=10)

my_text = Text(my_frame, font=our_font)
my_text.grid(row=0, column=0)
my_text.grid_rowconfigure(0, weight=1)
my_text.grid_columnconfigure(0, weight=1)

root.mainloop()
