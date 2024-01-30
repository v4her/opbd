from tkinter import *

def shopping_list():
    selected_items = listbox1.curselection()
    for item in selected_items:
        listbox2.insert(END, listbox1.get(item))
    selected_items = listbox1.curselection()
    for i in selected_items:
        listbox1.delete(i)

def product_list():
    selected_items = listbox2.curselection()
    for item in selected_items:
        listbox1.insert(END, listbox2.get(item))
    selected_items = listbox2.curselection()
    for i in selected_items:
        listbox2.delete(i)

root = Tk()

listbox1 = Listbox(root, selectmode=MULTIPLE)
items = ["Apple", "Bananas", "Carrot", "Bread", "Butter", "Meat", "Potato", "Pineapple"]
for item in items:
    listbox1.insert(END, item)
listbox1.pack(side=LEFT)

shopping_button = Button(root, text=">>>", command=shopping_list)
shopping_button.pack(side=LEFT)

product_button = Button(root, text="<<<", command=product_list)
product_button.pack(side=LEFT)

listbox2 = Listbox(root, selectmode=MULTIPLE)
items = ["Tomato", "Milk"]
for item in items:
    listbox2.insert(END, item)
listbox2.pack(side=RIGHT)

root.mainloop()