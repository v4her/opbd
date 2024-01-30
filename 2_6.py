import tkinter as tk
from tkinter import messagebox

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Заметки")
        self.notes = []
        self.current_note = None

        # Создаем виджеты для отображения заметок
        self.note_list = tk.Listbox(root)
        self.note_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.note_list.bind('<<ListboxSelect>>', self.on_note_select)

        # Создаем виджеты для редактирования заметок
        self.note_editor = tk.Text(root)
        self.note_editor.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Создаем кнопки для добавления, редактирования и удаления заметок
        self.add_button = tk.Button(root, text="Добавить", command=self.add_note)
        self.add_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.edit_button = tk.Button(root, text="Редактировать", command=self.edit_note)
        self.edit_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.delete_button = tk.Button(root, text="Удалить", command=self.delete_note)
        self.delete_button.pack(side=tk.BOTTOM, fill=tk.X)

    def on_note_select(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            self.current_note = self.notes[index]
            self.note_editor.delete('1.0', tk.END)
            self.note_editor.insert(tk.END, self.current_note)

    def add_note(self):
        new_note = self.note_editor.get('1.0', tk.END).strip()
        if new_note:
            self.notes.append(new_note)
            self.note_list.insert(tk.END, new_note)
            self.note_editor.delete('1.0', tk.END)

    def edit_note(self):
        if self.current_note:
            new_note = self.note_editor.get('1.0', tk.END).strip()
            if new_note:
                index = self.notes.index(self.current_note)
                self.notes[index] = new_note
                self.note_list.delete(self.note_list.curselection())
                self.note_list.insert(index, new_note)
                self.note_list.selection_set(index)
                self.current_note = new_note

    def delete_note(self):
        if self.current_note:
            index = self.notes.index(self.current_note)
            self.notes.remove(self.current_note)
            self.note_list.delete(index)
            self.current_note = None
            self.note_editor.delete('1.0', tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()