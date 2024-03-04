class Calculator:
    def __init__(self, real1, imag1, real2, imag2):
        # Инициализация объекта калькулятора с комплексными числами
        self.real1 = real1  # Действительная часть первого числа
        self.imag1 = imag1  # Мнимая часть первого числа
        self.real2 = real2  # Действительная часть второго числа
        self.imag2 = imag2  # Мнимая часть второго числа

    def add(self):
        # Сложение комплексных чисел
        return self.real1 + self.real2, self.imag1 + self.imag2

    def subtract(self):
        # Вычитание комплексных чисел
        return self.real1 - self.real2, self.imag1 - self.imag2

    def multiply(self):
        # Умножение комплексных чисел
        return self.real1 * self.real2 - self.imag1 * self.imag2, self.real1 * self.imag2 + self.real2 * self.imag1

    def divide(self):
        # Деление комплексных чисел
        denominator = self.real2 ** 2 + self.imag2 ** 2
        real_part = (self.real1 * self.real2 + self.imag1 * self.imag2) / denominator
        imag_part = (self.imag1 * self.real2 - self.real1 * self.imag2) / denominator
        return real_part, imag_part
