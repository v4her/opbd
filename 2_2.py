import tkinter as tk
from tkinter import messagebox
import threading
import time

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Таймер")
        self.master.geometry("300x150")

        self.time_entry = tk.Entry(master)
        self.time_entry.pack()

        self.start_button = tk.Button(master, text="Пуск", command=self.start_timer)
        self.start_button.pack()

        self.time_label = tk.Label(master, text="00:00")
        self.time_label.pack()

        self.running = False

    def start_timer(self):
        if not self.running:
            self.running = True
            user_input = self.time_entry.get()
            try:
                minutes, seconds = map(int, user_input.split(':'))
                total_seconds = minutes * 60 + seconds
                threading.Thread(target=self.countdown, args=(total_seconds,)).start()
            except ValueError:
                messagebox.showerror("Ошибка", "Неверный формат ввода. Используйте ММ:СС.")

    def countdown(self, total_seconds):
        while total_seconds > 0 and self.running:
            minutes, seconds = divmod(total_seconds, 60)
            self.time_label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.master.update()
            time.sleep(1)
            total_seconds -= 1

        if total_seconds == 0:
            messagebox.showinfo("Время вышло!", "Таймер закончил отсчет")
            self.time_label.config(text="00:00")
            self.running = False

    def stop_timer(self):
        self.running = False

def main():
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()