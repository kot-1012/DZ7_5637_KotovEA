import tkinter as tk
from calculator import Calculator

class GUI:
    def __init__(self, root):
        """
        Инициализация графического интерфейса.

        Args:
            root (tk.Tk): Основное окно.
        """
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

        # Фрейм для второго числа
        frame2 = tk.Frame(self.root)
        frame2.pack()

        self.real2_label = tk.Label(frame2, text="Действительная часть 2:")  # Метка для действительной части второго числа
        self.real2_label.grid(row=0, column=0)
        self.real2_entry = tk.Entry(frame2)  # Поле ввода для действительной части второго числа
        self.real2_entry.grid(row=0, column=1)

        self.imag2_label = tk.Label(frame2, text="Мнимая часть 2:")  # Метка для мнимой части второго числа
        self.imag2_label.grid(row=1, column=0)
        self.imag2_entry = tk.Entry(frame2)  # Поле ввода для мнимой части второго числа
        self.imag2_entry.grid(row=1, column=1)

        # Кнопки для выполнения операций
        self.operations_frame = tk.Frame(self.root)
        self.operations_frame.pack()

        self.add_button = tk.Button(self.operations_frame, text="Сложение", command=self.add)  # Кнопка для сложения
        self.add_button.grid(row=0, column=0)

        self.subtract_button = tk.Button(self.operations_frame, text="Вычитание", command=self.subtract)  # Кнопка для вычитания
        self.subtract_button.grid(row=0, column=1)

        self.multiply_button = tk.Button(self.operations_frame, text="Умножение", command=self.multiply)  # Кнопка для умножения
        self.multiply_button.grid(row=0, column=2)

        self.divide_button = tk.Button(self.operations_frame, text="Деление", command=self.divide)  # Кнопка для деления
        self.divide_button.grid(row=0, column=3)

    def get_input(self):
        """
        Получение введенных пользователем значений.
        
        Returns:
            tuple: Кортеж, содержащий действительные и мнимые части для обоих чисел.
        """
        real1 = float(self.real1_entry.get())
        imag1 = float(self.imag1_entry.get())
        real2 = float(self.real2_entry.get())
        imag2 = float(self.imag2_entry.get())
        return real1, imag1, real2, imag2

    def add(self):
        """
        Выполнение операции сложения.
        """
        real1, imag1, real2, imag2 = self.get_input()
        calculator = Calculator(real1, imag1, real2, imag2)
        result_real, result_imag = calculator.add()
        self.display_result(result_real, result_imag)

    def subtract(self):
        """
        Выполнение операции вычитания.
        """
        real1, imag1, real2, imag2 = self.get_input()
        calculator = Calculator(real1, imag1, real2, imag2)
        result_real, result_imag = calculator.subtract()
        self.display_result(result_real, result_imag)

    def multiply(self):
        """
        Выполнение операции умножения.
        """
        real1, imag1, real2, imag2 = self.get_input()
        calculator = Calculator(real1, imag1, real2, imag2)
        result_real, result_imag = calculator.multiply()
        self.display_result(result_real, result_imag)

    def divide(self):
        """
        Выполнение операции деления.
        """
        real1, imag1, real2, imag2 = self.get_input()
        calculator = Calculator(real1, imag1, real2, imag2)
        result_real, result_imag = calculator.divide()
        self.display_result(result_real, result_imag)

    def display_result(self, result_real, result_imag):
        """
        Отображение результата операции.
        
        Args:
            result_real (float): Действительная часть результата.
            result_imag (float): Мнимая часть результата.
        """
        result_str = f"Результат: {result_real} + {result_imag}j"
        self.result_label = tk.Label(self.root, text=result_str)
        self.result_label.pack()
