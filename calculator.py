import os
import datetime

class Calculator:
    def __init__(self, real1, imag1, real2, imag2):
        """
        Инициализация калькулятора с комплексными числами.
        
        Args:
            real1 (float): Действительная часть первого числа.
            imag1 (float): Мнимая часть первого числа.
            real2 (float): Действительная часть второго числа.
            imag2 (float): Мнимая часть второго числа.
        """
        self.real1 = real1
        self.imag1 = imag1
        self.real2 = real2
        self.imag2 = imag2
        self.log_file = "calculation_log.txt"  # Имя файла для логирования

    def add(self):
        """
        Сложение комплексных чисел.
        
        Returns:
            tuple: Кортеж, содержащий действительную и мнимую части результата.
        """
        result_real, result_imag = self.real1 + self.real2, self.imag1 + self.imag2
        self._log_operation("+", result_real, result_imag)  # Логирование операции
        return result_real, result_imag

    def subtract(self):
        """
        Вычитание комплексных чисел.
        
        Returns:
            tuple: Кортеж, содержащий действительную и мнимую части результата.
        """
        result_real, result_imag = self.real1 - self.real2, self.imag1 - self.imag2
        self._log_operation("-", result_real, result_imag)  # Логирование операции
        return result_real, result_imag

    def multiply(self):
        """
        Умножение комплексных чисел.
        
        Returns:
            tuple: Кортеж, содержащий действительную и мнимую части результата.
        """
        result_real = self.real1 * self.real2 - self.imag1 * self.imag2
        result_imag = self.real1 * self.imag2 + self.real2 * self.imag1
        self._log_operation("*", result_real, result_imag)  # Логирование операции
        return result_real, result_imag

    def divide(self):
        """
        Деление комплексных чисел.
        
        Returns:
            tuple: Кортеж, содержащий действительную и мнимую части результата.
        """
        denominator = self.real2 ** 2 + self.imag2 ** 2
        real_part = (self.real1 * self.real2 + self.imag1 * self.imag2) / denominator
        imag_part = (self.imag1 * self.real2 - self.real1 * self.imag2) / denominator
        self._log_operation("/", real_part, imag_part)  # Логирование операции
        return real_part, imag_part

    def _log_operation(self, operator, result_real, result_imag):
        """
        Логирование операции в файл.
        
        Args:
            operator (str): Оператор (например, "+", "-", "*", "/").
            result_real (float): Действительная часть результата.
            result_imag (float): Мнимая часть результата.
        """
        log_message = f"({self.real1} + {self.imag1}j) {operator} ({self.real2} + {self.imag2}j) = ({result_real} + {result_imag}j)\n"
        try:
            # Проверяем, существует ли файл логирования
            if not os.path.exists(self.log_file):
                # Если файл не существует, создаем его
                with open(self.log_file, "w") as f:
                    f.write("Лог операций:\n")
            # Открываем файл для добавления новой записи
            with open(self.log_file, "a") as f:
                f.write(log_message)
        except Exception as e:
            # Если возникла ошибка при записи в файл, выводим сообщение об ошибке
            print(f"Ошибка записи в файл логирования: {e}")
