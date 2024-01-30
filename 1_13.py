from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

def insertText():
    try:
        file_name = fd.askopenfilename()
        with open(file_name, 'r') as f:
            s = f.read()
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
    if messagebox.askyesno("Подтверждение", "Вы уверены что хотите очистить текст?"):
        text.delete(1.0, END)

root = Tk()
text = Text(root, width=50, height=25)
text.grid(columnspan=2)
b1 = Button(root, text="Открыть", command=insertText)
b1.grid(row=1, sticky=E)
b2 = Button(root, text="Сохранить", command=extractText)
b2.grid(row=1, column=1, sticky=W)
b3 = Button(root, text="Очистить", command=clearText)
b3.grid(row=1, column=2, sticky=W)
root.mainloop()