import tkinter as tk

class GUI:
    def __init__(self, root):
        # Инициализация графического интерфейса
        self.root = root  # Основное окно
        self.root.title("Калькулятор комплексных чисел")  # Заголовок окна
        self.create_widgets()  # Создание виджетов

    def create_widgets(self):
        # Фрейм для первого числа
        frame1 = tk.Frame(self.root)
        frame1.pack()

        self.real1_label = tk.Label(frame1, text="Действительная часть 1:")  # Метка для действительной части первого числа
        self.real1_label.grid(row=0, column=0)
        self.real1_entry = tk.Entry(frame1)  # Поле ввода для действительной части первого числа
        self.real1_entry.grid(row=0, column=1)

        self.imag1_label = tk.Label(frame1, text="Мнимая часть 1:")  # Метка для мнимой части первого числа
        self.imag1_label.grid(row=1, column=0)
        self.imag1_entry = tk.Entry(frame1)  # Поле ввода для мнимой части первого числа
        self.imag1_entry.grid(row=1, column=1)

        # Фрейм для операции и второго числа
        frame2 = tk.Frame(self.root)
        frame2.pack()

        self.operation_var = tk.StringVar()
        self.operation_var.set("+")
        self.operation_label = tk.Label(frame2, text="Операция:")  # Метка для выбора операции
        self.operation_label.grid(row=0, column=0)
        self.operation_menu = tk.OptionMenu(frame2, self.operation_var, "+", "-", "*", "/")  # Меню выбора операции
        self.operation_menu.grid(row=0, column=1)

        self.real2_label = tk.Label(frame2, text="Действительная часть 2:")  # Метка для действительной части второго числа
        self.real2_label.grid(row=1, column=0)
        self.real2_entry = tk.Entry(frame2)  # Поле ввода для действительной части второго числа
        self.real2_entry.grid(row=1, column=1)

        self.imag2_label = tk.Label(frame2, text="Мнимая часть 2:")  # Метка для мнимой части второго числа
        self.imag2_label.grid(row=2, column=0)
        self.imag2_entry = tk.Entry(frame2)  # Поле ввода для мнимой части второго числа
        self.imag2_entry.grid(row=2, column=1)

        # Кнопка для вычисления
        self.calculate_button = tk.Button(self.root, text="Вычислить", command=self.calculate)  # Кнопка для выполнения вычислений
        self.calculate_button.pack()

        # Метка для отображения результата
        self.result_label = tk.Label(self.root, text="")  # Метка для отображения результата вычислений
        self.result_label.pack()

    def calculate(self):
        # Функция для выполнения вычислений
        real1 = float(self.real1_entry.get())  # Получение действительной части первого числа из поля ввода
        imag1 = float(self.imag1_entry.get())  # Получение мнимой части первого числа из поля ввода
        real2 = float(self.real2_entry.get())  # Получение действительной части второго числа из поля ввода
        imag2 = float(self.imag2_entry.get())  # Получение мнимой части второго числа из поля ввода
        operation = self.operation_var.get()  # Получение выбранной операции из меню

        complex1 = complex(real1, imag1)  # Создание комплексного числа из полученных частей первого числа
        complex2 = complex(real2, imag2)  # Создание комплексного числа из полученных частей второго числа

        result = None  # Инициализация результата
        if operation == "+":
            result = complex1 + complex2  # Сложение
        elif operation == "-":
            result = complex1 - complex2  # Вычитание
        elif operation == "*":
            result = complex1 * complex2  # Умножение
        elif operation == "/":
            result = complex1 / complex2  # Деление

        self.result_label.config(text="Результат: " + str(result))  # Отображение результата на метке
