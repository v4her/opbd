from tkinter import *

def change_size(event=None):
    new_width = int(width_entry.get())
    new_height = int(height_entry.get())
    text.config(width=new_width, height=new_height)

def on_focus_in(event):
    text.config(bg="white")

def on_focus_out(event):
    text.config(bg="lightgrey")

root = Tk()

width_entry = Entry(root)
width_entry.grid(row=0, column=1)

height_entry = Entry(root)
height_entry.grid(row=1, column=1)

change_button = Button(root, text="Изменить", command=change_size)
change_button.grid(row=0, column=0, columnspan=2)

text = Text(root, bg="lightgrey")
text.grid(row=3, column=0, columnspan=2)

text.bind("<Return>", change_size)
text.bind("<FocusIn>", on_focus_in)
text.bind("<FocusOut>", on_focus_out)

root.mainloop()