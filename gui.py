import tkinter as tk

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор комплексных чисел")
        self.create_widgets()

    def create_widgets(self):
        # Фрейм для первого числа
        frame1 = tk.Frame(self.root)
        frame1.pack()

        self.real1_label = tk.Label(frame1, text="Действительная часть 1:")
        self.real1_label.grid(row=0, column=0)
        self.real1_entry = tk.Entry(frame1)
        self.real1_entry.grid(row=0, column=1)

        self.imag1_label = tk.Label(frame1, text="Мнимая часть 1:")
        self.imag1_label.grid(row=1, column=0)
        self.imag1_entry = tk.Entry(frame1)
        self.imag1_entry.grid(row=1, column=1)

        # Фрейм для операции и второго числа
        frame2 = tk.Frame(self.root)
        frame2.pack()

        self.operation_var = tk.StringVar()
        self.operation_var.set("+")
        self.operation_label = tk.Label(frame2, text="Операция:")
        self.operation_label.grid(row=0, column=0)
        self.operation_menu = tk.OptionMenu(frame2, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.grid(row=0, column=1)

        self.real2_label = tk.Label(frame2, text="Действительная часть 2:")
        self.real2_label.grid(row=1, column=0)
        self.real2_entry = tk.Entry(frame2)
        self.real2_entry.grid(row=1, column=1)

        self.imag2_label = tk.Label(frame2, text="Мнимая часть 2:")
        self.imag2_label.grid(row=2, column=0)
        self.imag2_entry = tk.Entry(frame2)
        self.imag2_entry.grid(row=2, column=1)

        # Кнопка для вычисления
        self.calculate_button = tk.Button(self.root, text="Вычислить", command=self.calculate)
        self.calculate_button.pack()

        # Метка для отображения результата
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def calculate(self):
        real1 = float(self.real1_entry.get())
        imag1 = float(self.imag1_entry.get())
        real2 = float(self.real2_entry.get())
        imag2 = float(self.imag2_entry.get())
        operation = self.operation_var.get()

        complex1 = complex(real1, imag1)
        complex2 = complex(real2, imag2)

        result = None
        if operation == "+":
            result = complex1 + complex2
        elif operation == "-":
            result = complex1 - complex2
        elif operation == "*":
            result = complex1 * complex2
        elif operation == "/":
            result = complex1 / complex2

        self.result_label.config(text="Результат: " + str(result))
