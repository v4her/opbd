import tkinter as tk
from PIL import Image, ImageTk
import random

def move_button():
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    new_x = random.randint(0, window_width - button.winfo_width())
    new_y = random.randint(0, window_height - button.winfo_height())

    button.place(x=new_x, y=new_y)
root = tk.Tk()
root.geometry("800x600")
image = Image.open("knife.gif")
photo = ImageTk.PhotoImage(image)
button = tk.Button(root, image=photo, command=move_button)
button.place(x=0, y=0)

root.mainloop()