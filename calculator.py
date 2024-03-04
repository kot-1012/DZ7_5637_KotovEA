class Calculator:
    def __init__(self, real1, imag1, real2, imag2):
        self.real1 = real1
        self.imag1 = imag1
        self.real2 = real2
        self.imag2 = imag2

    def add(self):
        return self.real1 + self.real2, self.imag1 + self.imag2

    def subtract(self):
        return self.real1 - self.real2, self.imag1 - self.imag2

    def multiply(self):
        return self.real1 * self.real2 - self.imag1 * self.imag2, self.real1 * self.imag2 + self.real2 * self.imag1

    def divide(self):
        denominator = self.real2 ** 2 + self.imag2 ** 2
        real_part = (self.real1 * self.real2 + self.imag1 * self.imag2) / denominator
        imag_part = (self.imag1 * self.real2 - self.real1 * self.imag2) / denominator
        return real_part, imag_part
