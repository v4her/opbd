from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

def insertText():
    try:
        file_name = fd.askopenfilename()
        with open(file_name, 'r') as f:
            s = f.read()
            text.delete(1.0, END)
            text.insert(1.0, s)
    except:
        messagebox.showinfo("Информация", "Файл не выбран")

def extractText():
    try:
        file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"), ("HTML files", "*.html;*.htm"), ("All files","*.*")))
        with open(file_name, 'w') as f:
            s = text.get(1.0, END)
            f.write(s)
    except:
        messagebox.showinfo("Информация", "Файл не сохранился")

def clearText():
    text.delete(1.0, END)

root = Tk()
text = Text(root, width=50, height=25)
text.grid(columnspan=2)

# Create a menu
menu = Menu(root)
root.config(menu=menu)

# Create a file menu
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=insertText)
file_menu.add_command(label="Сохранить", command=extractText)

# Create a context menu
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Очистить", command=clearText)

def on_right_click(event):
    try:
        context_menu.tk_popup(event.x_root, event.y_root)
    finally:
        context_menu.grab_release()

text.bind("<Button-3>", on_right_click)

root.mainloop()