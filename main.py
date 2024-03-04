import tkinter as tk
from gui import GUI

if __name__ == "__main__":
    root = tk.Tk()  # Создание основного окна
    app = GUI(root)  # Создание объекта графического интерфейса
    root.mainloop()  # Запуск главного цикла обработки событий
