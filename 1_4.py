from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Текстовый редактор')
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as f:
            t.delete('1.0', END)
            t.insert(END, f.read ())
def save_file():
    file_path = e.get()
    if file_path:
        with open(file_path, 'w') as f:
            f.write(t.get('1.0', END))
            t.delete('1.0', END)
            e.delete(0, END)

entry_frame = Frame(root)
entry_frame.pack(fill=X)

Label(entry_frame, text='').pack(side=LEFT)

e = Entry(entry_frame)
e.pack(side=LEFT, fill=X, expand=True)

t = Text(root)
t.pack(fill=BOTH, expand=True)

button_frame = Frame(root)
button_frame.pack(fill=X)

Button(button_frame, text='Открыть', command=open_file).pack(side=LEFT)
Button(button_frame, text='Сохранить', command=save_file).pack(side=LEFT)

root.mainloop()